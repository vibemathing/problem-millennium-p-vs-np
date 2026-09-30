"""Deterministic local candidate checks; no mathematical admission authority."""
import itertools as it, json, sys
from fractions import Fraction

def sat(F, assignment):
    return all(any(assignment[abs(x)] == (x>0) for x in C) for C in F)
def elim(F,x):
    pos=[C-{x} for C in F if x in C]
    neg=[C-{-x} for C in F if -x in C]
    out={C for C in F if x not in C and -x not in C}
    for A in pos:
        for B in neg:
            C=A|B
            if not any(-l in C for l in C): out.add(C)
    return out

def pnp_checks():
    # Exhaust all non-tautological clauses, including empty, in three variables;
    # exhaust all formulas of at most three distinct clauses and every first pivot.
    clauses=[frozenset((i+1)*s for i,s in enumerate(signs) if s) for signs in it.product((-1,0,1), repeat=3)]
    count=checks=0
    for size in range(4):
        for tup in it.combinations(clauses,size):
            F=set(tup); count+=1
            for x in (1,2,3):
                G=elim(F,x)
                others=[y for y in (1,2,3) if y!=x]
                for bits in it.product((False,True),repeat=2):
                    a=dict(zip(others,bits))
                    lhs=any(sat(F,a|{x:b}) for b in (False,True))
                    assert lhs==sat(G,a),(F,x,a,G)
                    checks+=1
            for order in it.permutations((1,2,3)):
                G=F
                for x in order: G=elim(G,x)
                direct=any(sat(F,dict(zip((1,2,3),bits))) for bits in it.product((False,True),repeat=3))
                assert direct == (frozenset() not in G)
    # Formula with 2k input clauses generates k^2 distinct resolvents at first pivot.
    wide={frozenset((1,2,3)),frozenset((-1,4,5))}
    wide_projection=elim(wide,1)
    assert wide_projection=={frozenset((2,3,4,5))}
    for bits in it.product((False,True),repeat=4):
        a=dict(zip((2,3,4,5),bits))
        assert sat(wide_projection,a)==any(sat(wide,a|{1:b}) for b in (False,True))
    blowup=[]
    for k in range(1,9):
        F={frozenset((1,2+i)) for i in range(k)}|{frozenset((-1,2+k+j)) for j in range(k)}
        G=elim(F,1); assert len(G)==k*k
        blowup.append({'k':k,'input_clauses':len(F),'resolvents':len(G)})
    return {'formulas':count,'pointwise_projection_checks':checks,'full_order_checks':count*6,'one_step_blowup':blowup,'width_3_to_4_regression':True,'width_regression_assignments':16}


if __name__=='__main__':
    print(json.dumps({'python':sys.version.split()[0], 'claim_ceiling':'bounded local regression only', 'pnp':pnp_checks()},indent=2))

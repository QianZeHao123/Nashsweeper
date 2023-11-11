# Regret-base Value Algorithm for Nashsweeper
## 0x01 Mathematical Implementation
In Nashsweeper, we adopt the regret-based algorithm proposed by Corley (2020) and others in recent years to calculate Nash equilibrium. It is an enumeration algorithm, and the core is the regret function $r_i$, which is expressed as follows:
$$r_i(s)=max_{s_{i}^{'} \in S_i}(s_{i}^{'},s_{-i})-u_i(s_i,s_{-i})$$
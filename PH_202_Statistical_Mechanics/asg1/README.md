# PH 202: Assignment 1

### **Name: Suman Kumar Pal**

### **Integrated Ph.D. (1st year)**

### **SR No.: 24974**

# Numerical Assignment

## Question 6
$$M_i = \left|i-\frac{Ns}{2}\right| + 5$$
- Arrays are created containing section numbers, time: `i_array` and `t_array`.
- Number of compartments are computed using given formula and the results are saved in an array: `M_array`.
- For each steps, the boxes are distributed. Number of boxes in compartments and compartments in section are saved in `Nb_array` (a 3d array). The total number of boxes in a section is saved  in `Nbt_array` (a 3d array).
- The plots are done.

## Question 7
$$F = \sum_i \sigma_i$$
- First 100 iteration results are taken from the previous code: `Nb100` (containing all boxes distribution) and `t100`.
- For these distributions, mean and variance are calculated. $F$ is calculated using given formula. (`ni_array`, `sigi_array`, `F_array`)
- $F$ vs $t$ is plotted to show that, $F$ also doesn't have any certain dependence on $t$.
- To plot $F$ for different $N_b$, a function `fn_ni_sigi_avg(Nb)` is defined. This function gives average mean and standard deviation as output for 100 iterations.
- Using the above function, $F$ is calculated for different $N_b$ and the plots are shown.

## Question 8
$$F_2 = \sum_i \frac{\sigma_i}{n_i}$$
- From the defined function `fn_ni_sigi_avg(N_b)`, mean ($n_i$) and standard deviation ($\sigma_i$) are calculated and from that $F_2$ is calculated using the given formula.
- The plots are shown.

## Conclusion

From the last plot, $F_2 = \sum_i \frac{\sigma_i}{n_i}$ is proportional to $\frac{1}{\sqrt{N_b}}$. From the plot in Question 7, $F = \sum_i \sigma_i$ is proportional to $\sqrt{N_b}$. Thus, $n_i$ is propotional to $N_b$. The obtained relations are, 
- $F \propto \sqrt{N_b}$
- $F_2 \propto \frac{1}{\sqrt{N_b}}$

This shows, if $N_b$ is large, although the fluctuation $F$ increases, the quantity 'fluctuation per mean' (i.e. $F_2$) decreases. It's actually the *central limit theorem*. The mean increases as $N_b$ and the standard deviation increases as $\sqrt{N_b}$. So, the quantity 'standard deviation per mean' decreases as $\frac{1}{\sqrt{N_b}}$. Thus, in higher limit of $N_b$ the preciseness of determining a quantity increases. This shows the behaviour of a system at thermodynamic limit (where, $N$ has the order $10^{23}$, a very very large number).

**Low $N_b$ effect:** 

For lower number of the boxes, many of the compartments will not be filled. Even, for very low $N_b$, some sections may remain unfilled. This implies, for low number limit, many of the states remains unfilled. If we have $N_b=1$, only 1 compartment or 1 section is filled. And for this, the disorderness is 0. This corresponds to the 3rd law of thermodynamics: "at absolute zero, number of microstates is 1 and the absolute entropy (which is the measure of disorderness) is $S = k_B \ln{1} = 0$".


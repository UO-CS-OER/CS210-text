---
jupytext:
  formats: md:myst
  text_representation:
    extension: .myst
    format_name: myst
    format_version: 1.1
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Successive Approximation

Suppose you had a machine that was not very smart, but could compute 
things and check certain simple conditions very quickly.  You might 
call such a machine a "computer".  If you directed it carefully, 
with something you might call a "program", you might even make it 
appear smart, although really it would just be doing a lot of simple 
operations.  For example, you could direct it to guess an answer 
(very badly!) and then make minor adjustments to improve its guess, 
until the refined guess looked like a smart answer.  If it could do 
this quickly enough, it might even appear to be making smart choices. 

Making a guess and then improving it is a basic optimization 
technique for many simulations of physical systems.  The initial 
guess does not have to be good, provided we have some way of 
improving it, and improving it again, and so on until we have 
reached a good solution.  Systems for setting the timing of traffic 
lights to optimize traffic work this way ... it is likely that 
the timing of traffic lights in your current city was selected by the
[Transyt](https://en.wikipedia.org/wiki/TRANSYT-7F) system, whose 
core method is exactly this.   

```{note}
I chose the Transyt software as an example 
because I know it was 
used to set the light timings in Eugene, Oregon decades ago.  I know
because my first assignment as a junior programmer was to make
that software work on the IBM mainframe computer then used by the city.
I encountered Transyt again several years later, when my spouse
was working for a transportation research group at University of California, Irvine. 
Useful programs last a long time, and evolve, sometimes through 
generations of programmers.  The Transyt system today is likely 
different in many ways than the code I encountered 40+ years ago.  
It may have been completely rewritten in a more modern programming 
language (or maybe not).  Almost certainly, though, the core 
method "guess and refine" approach to optimization remains the same. 
-MY
```

Simulations of physical systems are complex, but we can illustrate 
the approach more simply with a "system" that is just a math 
formula.  Suppose we wanted to find the square root of a number 
greater than 1.0.   Suppose all we knew is that 

$$ \sqrt{n} * \sqrt{n} = n $$

and that, for numbers greater than 1, $m > n \implies m^2 > n^2$.  
This is enough to get very close to a correct answer by 
making a guess and refining it.  (Exactly how close we can get is 
complicated, because the computer uses a floating-point 
approximation to real numbers.)

```{code-cell} python3
def guess_sqrt(n: float, error_bound: float) -> float: 
    """n must be between 1.0 and 100,000. 
    error_bound must be greater than  0.00001
    Returns a number q such that 
    q^2 - error_bound <= n <= q^2 + error_bound.
    """
    # q must be between 1 and n
    q_max = n
    q_min = 1.0
    # Execute the loop at least once
    error = 2 * error_bound
    while error > error_bound: 
        # Make a guess within bounds
        q = (q_min + q_max) / 2.0
        # How bad is it? 
        error = abs(q*q - n)
        print(f"Guessed sqrt({n}) ≅ {q}")
        print(f"\t off by {error}")
        # Improve the guess by squeezing the bounds
        if q*q > n:
            # Too big! 
            q_max = q
        else: 
            # Too small! 
            q_min = q 
    return  q
    
s = guess_sqrt(2.0, .0001)
print(s)
```

In math courses you may encounter the Newton-Raphson method for 
estimating roots of a polynomial, using a better refinement to the 
guess in each iteration than I have used above, and other series 
that are essentially variations of this "guess and refine" approach. 

If we don't have a direct way of checking the error bound as we did 
by squaring `q`, but we have upper and lower bounds on the answer
(like `q_max` and `q_min` above), then we can infer that the error 
is at most `q_max - q_min`. 

If we cannot even set some kinds of bounds around a solution 
(perhaps because the solution is not a number, but something more 
complex), we can at least determine whether we are getting the same 
guess or something different from iteration to iteration.  If our 
guess is not changing, there is no point in continuing.  

In our 
[clustering project](https://github.com/UO-CS210/wildfire), we stop 
the loop when the assignment of locations to clusters stops changing. 
Usually this will be a pretty good solution, but it is not 
guaranteed. When the k-means clustering algorithm is used in 
practice, it is often run more than once with different initial 
guesses to increase the chance that it produces at least one very 
good solution. 

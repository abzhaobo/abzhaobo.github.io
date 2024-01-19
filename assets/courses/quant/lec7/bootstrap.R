rm(list=ls())
# ==========================================================================
# Bootstrap
# ==========================================================================
n <- 10
x <- rnorm(n) # Norm(0,1) distribution, 10 points
print(x)
#
# We want to check the bootstrap sample std of the sample mean
#
### n-sample mean and n-sample std, the analytical solution
x_mean <- mean(x) # n-sample mean
x_std <- sd(x) # n-sample standard deviation
x_mean_std <- x_std/sqrt(n)
x_mean_std
### The bootstrapped sample, (b-sample)
B <- 10000
boot <- list()
for (i in 1:B){
    boot[[i]] <- sample(x, n, replace=TRUE, prob=rep(1/n,n))
}
print(boot[[sample(1:10000, 1)]])
boot_mean <- lapply(boot,mean) # Calculate the n-sample mean for each of the 10000 b-samples
length(boot_mean)
boot_mean <- unlist(boot_mean)

x_mean_std_boot <- sqrt(sum((boot_mean - mean(boot_mean))^2)/B) # This is the b-sample std of the bootstrapped mean. It should be similar to x_mean_std, which is obtained analytically.
x_mean_std_boot

#
# We also see that when n is small, x is not good enough to represent N(0,1) distribution. 
#
x_mean # should be close to 0 if n is large
x_mean_std # should be close to 1/sqrt(10) 
x_mean_std_true <- 1/sqrt(n)

print(c(x_mean_std_true, x_mean_std, x_mean_std_boot))
### The difference of the first and the second is determined by n; the difference of the second and the third is determined by B

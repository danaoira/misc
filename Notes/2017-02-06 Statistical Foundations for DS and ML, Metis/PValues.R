library(ggplot2)
library(plotly)
# estimated model is: y = a0 + a1*x + e

obs<-100                # obs in each single regression
Nloops<-1000            # number of experiments
output<-numeric(Nloops) # vector holding p-values of estimated a1 parameter from Nloops experiments

for(i in seq_along(output)){
  
  x<-rnorm(obs) 
  y<-rnorm(obs)
  
  # x and y are independent, so null hypothesis is true
  output[i] <-(summary(lm(y~x)) $ coefficients)[2,4] # we grab p-value of a1
  
  if(i%%100==0){cat(i,"from",Nloops,date(),"\n")} # after each 100 iteration info is printed
  
}


plot(hist(output), main="Histogram of p-values")

m <- ggplot(data.frame(pvals = output), aes(x = pvals, y = ..count..)) + geom_histogram(binwidth = 0.05, aes(fill = ..count..))+
  scale_x_continuous(limits = c(0, 1)) + ggtitle("p-value histogram")
m
ks.test(output,"punif") # Null hypothesis is that output distr. is uniform


plotlyDF <- data.frame(regression = 1:Nloops, pval = output)

plot_ly(data = plotlyDF, x = ~regression, y = ~-log(pval,10), name = 'logP',type = 'scatter', mode = 'markers') %>% 
  add_trace(x=c(0,1000), y= -log(.05, 10), mode = "lines")

sum(output <= .05)

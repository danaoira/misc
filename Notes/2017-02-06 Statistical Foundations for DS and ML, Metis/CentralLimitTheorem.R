numSamples <- 1000
obsPerSample <- 1000



###Uniform Distr
resultsUniform <- unlist(lapply(1:numSamples, function(x){
            return(mean(
              runif(obsPerSample, min = 0, max = 100)
            )
          )
          }))

resultsExponential <- unlist(lapply(1:numSamples, function(x){
  return(mean(
    rexp(obsPerSample, rate = 1/50)
  ))
}))

resultsBinom <- unlist(lapply(1:numSamples, function(x){
  return(mean(
    rbinom(obsPerSample, size = 1, prob = .2)
  ))
}))


shapiro.test(resultsUniform)


shapiro.test(resultsExponential)
shapiro.test(resultsBinom)

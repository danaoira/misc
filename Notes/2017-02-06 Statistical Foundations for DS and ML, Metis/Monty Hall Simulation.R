library(dplyr)

numSims <- 10000
numDoors <- 1:3

myDF <- data.frame(winningDoor = sample(x = numDoors, size = numSims, replace = TRUE),
                   initialChoice = sample(x = numDoors, size = numSims, replace = TRUE)) 

myDF$openedDoor <- apply(myDF, 1, function(x){
  optionsToChoose <- setdiff(numDoors, as.numeric(x))
  if(length(optionsToChoose) == 1){
    return(optionsToChoose)
  }else{
    return(sample(optionsToChoose,1)) 
  }
})

myDF$selectedDoor <- apply(myDF, 1, function(x){
  return(sample(setdiff(numDoors, x['openedDoor']), 1))
})

myDF <- myDF %>% 
  mutate(NoSwitch = ifelse(selectedDoor == initialChoice, 1, 0))


sum((myDF$selectedDoor == myDF$winningDoor & myDF$NoSwitch==1))/sum(myDF$NoSwitch ==1)
sum((myDF$selectedDoor == myDF$winningDoor & myDF$NoSwitch==0))/sum(myDF$NoSwitch ==0)


install.packages("dplyr")
library(dplyr)
install.packages("readr")
library(readr)
install.packages("tidyverse")
library(tidyverse)


getwd #Checking current directory
setwd("C:/Users/Faisal/Desktop/EDUCATION/Semester 4/CSC 3305 DATA SCIENCE") #Set new directory
data <- read.csv("dataset-preprocessed.csv") #Load data frame unto data
data$DIFFERENCE <- (data$JULY - data$JUNE) #Subtract between July and June to find price changes
data$CODE <- c("Clean C","Super C","Live C", "Imported TC", "Live OC", "Wings C", "Meat G", "Imported BM", "Boneless IM","Imported BG", "Local BT", "Local BS", "Import BF", "P Belly", "P Meat", "F Local", "F Selayang", "Cob/Aya/Wood", "L White S/ Banana", "Cabbage", "Tomato", "Red Chili", "Green Pepper", "Coconut", "GR Coconut", "A Eggs","B Eggs", "C Eggs", "Imported O", "Red O", "Red O Rose", "Garlic", "Dhal", "Potatoes")
View(data[, c("DESCRIPTION.OF.GOODS","CODE","JUNE","JULY","DIFFERENCE") ]) #View the table's current situation 

diff <- data$DIFFERENCE #The variable diff will copy the values in column "DIFFERENCE"
totaldiff <- sum(diff) #To find the total of diff variable since this signify the sum of positive changes of the prices
data$PERCENTAGE <- ((data$DIFFERENCE / totaldiff) * 100) #The formula to find the percentage of items contribution to the price increase
View(data[, c("DESCRIPTION.OF.GOODS","JUNE","JULY","DIFFERENCE","PERCENTAGE") ]) #View the table's current situation 
pcent <- data$PERCENTAGE #The values of column PERCENTAGE will be copied into variable pcent
pcent[pcent<0] <- 0 #All negative values of variable diff will be changed to 0 
data$PERCENTAGE <- pcent 
library(dplyr)
data <- data %>% filter(data$PERCENTAGE != 0) #All data in the column PERCENTAGE with 0 value will be cut out from the column 
View(data[, c("DESCRIPTION.OF.GOODS","CODE","DIFFERENCE", "PERCENTAGE") ]) #View the table's current situation 

library(ggplot2)
finalp <- format(round(data$PERCENTAGE, 2), nsmall = 2)
finalp
k <- ggplot(data, aes(CODE,finalp,label = finalp))+geom_bar(stat = "identity") + geom_text(size=5, vjust = -1,color = "purple") + ggtitle("Item that contributed most to the net price increase in the month of July") + xlab("Controlled Goods") + ylab("Percentage contributed")+ geom_col(width = 0.2)
k + theme(
  plot.title = element_text(color="red", size=14, face="bold.italic"),
  axis.title.x = element_text(color="blue", size=14, face="bold"),
  axis.title.y = element_text(color="#993333", size=14, face="bold")
)






#get the dataset
#read the csv file
data = read.csv("../hw1_data.csv")

#get the columns names from the dataset
names(data)
#first two rows
head(data,2)
#last two rows
tail(data,2)

#observations (i.e. rows) are in this data frame
nrow(data)

#value of Ozone in the 47th row
data[[47,1]]

#count number of missing values in Ozone column
missing <- subset(data,is.na(Ozone))
nrow(missing)

#get the mean of the column Ozone
osub <- subset(data,!is.na(Ozone),select = Ozone)
apply(osub, 2, mean)


#mean of colum Solar.R given condition
sosub <- subset(data,Ozone>31 & Temp>90,select = Solar.R)
apply(sosub,2,mean)

#mean of Temp given condition
tempsub <- subset(data,Month==6,select = Temp)
apply(tempsub,2,mean)

#maximum element in Ozone column given condition
ozone_max_sub <- subset(data,Month==5 & !is.na(Ozone),select = Ozone)
apply(ozone_max_sub,2,max)




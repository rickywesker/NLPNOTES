#Plotting Graph
boxplot(d$ARA~d$ST,xlab = "ST or not",ylab = "ARA",col = "lightblue")
boxplot(d$ASSET~d$ST,xlab = "ST or not",ylab = "Asset",col = "lightblue")
boxplot(d$GROWTH~d$ST,xlab = "ST or not",ylab = "Growth",col = "lightblue")

par(mfrow=c(2,2))
boxplot(d$ATO~d$ST,xlab = "ST or not",ylab = "ATO",col = "lightblue")
boxplot(d$ROA~d$ST,xlab = "ST or not",ylab = "ROA",col = "lightblue")
boxplot(d$LEV~d$ST,xlab = "ST or not",ylab = "LEV",col = "lightblue")
boxplot(d$SHARE~d$ST,xlab = "ST or not",ylab = "Share",col = "lightblue")



#Building Model
#standarizaion of TrainSet
tmp1 = stockTrain[,c(1:7)]#features
tmp1 = as.data.frame(scale(tmp1))
tmp1 = cbind(tmp1,stockTrain$ST)

#standarization of TestSet
tmp2 = stockTest[,c(1:7)]
tmp2 = as.data.frame(scale(tmp2))
tmp2 = cbind(tmp2,stockTest$ST)

#logistic Regression
fit = glm(stockTrain$ST~ARA+ASSET+ATO+ROA+GROWTH+LEV+SHARE,family = binomial(link = logit),data = stockTrain)
summary(fit)

#predict
stockTest$prob = exp(predict(fit,tmp2))/(1+exp(predict(fit,tmp2)))
#Plot
library(pROC)
g <- roc(stockTest$ST~stockTest$prob)
plot(g,print.auc=TRUE,auc.polygon=TRUE)

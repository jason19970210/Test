library(xml2)
library(dplyr)
library(plotly)
library(ggplot2)

pm2 <- read.csv("https://raw.githubusercontent.com/jason19970210/Test/master/PM25/pm25.csv",stringsAsFactors = F)

pm2 %>% plot_ly(x = .$CO, y = .$CO_8, type = 'scatter', mode = 'markers')
pm2 %>% plot_ly(x = .$O3, y = .$O3_8, type = 'scatter', mode = 'markers')
pm2
ggplot(data = pm2, aes(x = O3, y = O3_8)) + geom_point() + geom_smooth(lm(pm2$O3_8~pm2$O3))

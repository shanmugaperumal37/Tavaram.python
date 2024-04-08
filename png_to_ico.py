import matplotlib.pyplot as p
year=[2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
acp=[91, 90, 90, 98, 99, 89, 78, 98, 99, 100]
p.plot(year,acp,marker="o",mec="green",mfc="green")
p.xlabel("past 10 years")
p.ylabel("Academic performance")
p.show()


# How Use

<head>
  <meta charset="UTF-8">
  <meta name="description" content="Free tracking for COVID-19 in world">
  <meta name="keywords" content="HTML,Python">
  <meta name="author" content="Manuel Ferreira Junior">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head> 

## Clone

How clone this repository
```{git}
-----------------------------------------------------------------------------------------------------------------
$ git clone https://github.com/Manuelfjr/Covid19.git 
-----------------------------------------------------------------------------------------------------------------
```

## Features

### World maps

That feature necessary open cmd in Covid/worldmps, or copy
```{git}
-----------------------------------------------------------------------------------------------------------------
$ cd Covid19/worldmps

$ python wmps.py -h
-----------------------------------------------------------------------------------------------------------------
```
The command "-h" show help for use (show the arguments).
```{git}
-----------------------------------------------------------------------------------------------------------------
 -h, --help           		: show help message, and arguments

 -r RUN, --run RUN    		: run all code (default: True)

 -a ALL, --all ALL		: boolean value, if True, create local
				host for all maps, if False, creat
				local host for the "TYPE"
				(default: False)

 -d DATE, --date DATE		: the day how reference to create
				world maps. (default: 6/10/20) 

 -b BOOL, --bool BOOL    	: boolean value. Do you have datasets ?!
			  	if True, continue, if False, download
		 		datasets. (default: False)

 -f FOLDER, --folder FOLDER	: folder name for datasets.
				(default: dataworld)

 -t TYPE, --type TYPE 		: type confirmed, recovered or deaths.
				- cwm == 'confirmed'
				- rwm == 'recovered'
				- dwm == 'deaths'
				(default: cwm)
-----------------------------------------------------------------------------------------------------------------
```
#### Example (confirmed cases of world):

![gif](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/.others/.cwm.gif)

### All 

the all.py generate all graphs on terminal. Usage:

```{git}
-----------------------------------------------------------------------------------------------------------------
$ cd Covid/all

$ python all.py -h 
-----------------------------------------------------------------------------------------------------------------
```
-h argument for help needed for other arguments. Optional arguments:
```{git}
-----------------------------------------------------------------------------------------------------------------
 -h, --help            		: show this help message and exit

 -all ALL, --all ALL   		: run all (default: True)

 -d DATE, --date DATE  		: date by US type (default: 6/11/20)

 -dbr DATEBR, --datebr DATEBR	: date by brazillian type (default: 11/6)

 -dys DAYS, --days DAYs   	: countries number (default: 30)

 -w WEEKS, --weeks WEEKS  	: today (default: 5)

 -nw N_WEEKS, --n_weeks N_WEEKS : number weeks (default: 14)

 -nc NC, --numcountries NC 	: countries number (default: 6)

 -n N, --numstates N   		: states number of Brazil (top n) 
				(default: 10)
-----------------------------------------------------------------------------------------------------------------
```
# Growth charts and percentages
Analysis of the growth in the number of contaminated, dead and recovered, for the world, especially for Brazil

# Graphics

## Cases
![1](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/confirmedcovid.png)

## Deaths
![2](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/deathscovid.png)

## Recovered
![3](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/revoredcovid.png)

# Brazil

## Region

### Cases

* Region

Accumulated cases 
![4](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/cumconfirmregion.png)

Increase from one day to the next (last 30 days)
![5](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/confirmratedaysregion.png)

average increment from one day to the next, for the last 5 weeks
![6](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/confirmrateweeksregion.png)

* State
Accumulated cases 
![7](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/cumconfirmstate.png)

Increase from one day to the next (last 30 days)
![8](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/confirmratedaysstate.png)

average increment from one day to the next, for the last 5 weeks
![9](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/confirmrateweeksstate.png)


### Deaths

* Region

Accumulated deaths 
![10](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/cumdeathsregion.png)

Increase from one day to the next (last 30 days)
![11](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/deathsratedaysregion.png)

average increment from one day to the next, for the last 5 weeks
![12](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/deathsrateweeksregion.png)

* State
Accumulated cases 
![13](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/cumdeathsstate.png)

Increase from one day to the next (last 30 days)
![14](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/deathsratedaysstate.png)

average increment from one day to the next, for the last 5 weeks
![15](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/deathsrateweeksstate.png)

* Heatmaps

Heatmap of the correlation between deaths, by region
![16](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/heatmapregiondeathscorr.png)

Heat map of the average increase in deaths, from one day to the next, in the last weeks
![17](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/heatmapregionweeksdeathscorr.png)

* Letality

Letality rate (for World)
![18](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/letalityrate.png)

Letality rate (for Brazil, by region)
![19](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/letalityratebrregion.png)

Letality rate (for Brazil, by state)
![20](https://raw.githubusercontent.com/Manuelfjr/Covid19/master/all/images/letalityratebrstate.png)

* World maps

[Confirmeds]()

[Deaths]()

[Recovered]()

# Growth

<blockquote style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/2713318/?utm_source=embed&utm_campaign=visualisation/2713318' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a><p>Beautiful, easy data visualization and storytelling</p></blockquote>


<blockquote class="embedly-card"><h4><a href="https://public.flourish.studio/visualisation/2702302/">Crescimento de casos confirmados por COVID-19 no Brasil (Por Estado)</a></h4><p>Bar chart race. Confirmed cases by State.</p></blockquote>

<blockquote class="embedly-card"><h4><a href="https://public.flourish.studio/visualisation/2702550/">Crescimento de casos confirmados por COVID-19 no Brasil (Por Região)</a></h4><p>Bar chart race. Confirmed cases by Region.</p></blockquote>

<blockquote class="embedly-card"><h4><a href="https://public.flourish.studio/visualisation/2713318/">Crescimento de mortos por COVID-19 no Brasil (Por Estado)</a></h4><p>Bar chart race. Deaths by State.</p></blockquote>

<blockquote class="embedly-card"><h4><a href="https://public.flourish.studio/visualisation/2713121/">Crescimento de mortos por COVID-19 no Brasil (Por Região)</a></h4><p>Bar chart race. Deaths by Region.</p></blockquote>




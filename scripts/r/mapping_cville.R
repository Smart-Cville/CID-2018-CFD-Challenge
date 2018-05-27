################################################################################
##
## <PROJ> CID 2018: CFD Challenge
## <FILE> mapping_cville.R
## <AUTH> Benjamin Skinner @btskinner
## <INIT> 27 May 2018
##
################################################################################

## PURPOSE -----------------------------------------------------------
##
## This script is a template for using the Charlottesville Open Data
## portal to get and map spatial data in R.
##
## -------------------------------------------------------------------

## clear memory
rm(list = ls())

## libraries
libs <- c('tidyverse','sf','leaflet','RColorBrewer')
lapply(libs, require, character.only = TRUE)

## base cville open data portal url
base_url <- 'https://opendata.arcgis.com/datasets/'

## ------------------------------------------
## get spatial neighborhood data
## ------------------------------------------

## Charlottesville neighborhoods in geojson
url <- paste0(base_url, 'ceaf5bd3321d4ae8a0c1a2b21991e6f8_9.geojson')

## read data
df_nb <- st_read(url) %>%
    ## lower names
    rename_all(tolower) %>%
    ## add random fill_id for mapping
    mutate(fill_id = factor(sample.int(12L, n(), replace = TRUE)))

## set up color palette that will align with indices
factpal <- colorFactor(palette = brewer.pal(n = 12L, name = 'Paired'),
                       domain = df_nb$fill_id)


## make leaflet map
m <- leaflet(df_nb) %>%
    addProviderTiles(providers$CartoDB.Positron) %>%
    addPolygons(color = 'black', weight = 2,
                fillOpacity = .5, fillColor = ~factpal(df_nb$fill_id),
                label = ~name)
m

## ------------------------------------------
## get firestation locations
## ------------------------------------------

## crime incidents
url <- paste0(base_url, '1e88883200df44798c5cfc303a9ed9d4_8.geojson')

## read data
df_fs <- st_read(url) %>%
    ## lower names
    rename_all(tolower)

## add to map
m <- m %>%
    addMarkers(data = df_fs, label = ~name)
m

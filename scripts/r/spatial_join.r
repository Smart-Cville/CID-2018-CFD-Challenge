################################################################################
##
## <PROJ> CID 2018: CFD Challenge
## <FILE> spatial_join.R
## <AUTH> Benjamin Skinner @btskinner
## <INIT> 2 June 2018
##
################################################################################

## PURPOSE -----------------------------------------------------------
##
## This script is a template for using the Charlottesville Open Data
## portal to join spatial data in R.
##
## -------------------------------------------------------------------

## clear memory
rm(list = ls())

## libraries
libs <- c('tidyverse','sf','leaflet','RColorBrewer')
lapply(libs, require, character.only = TRUE)

## base cville open data portal url
base_url <- 'https://opendata.arcgis.com/datasets/'

## directories
ddir <- '../../data'

## ------------------------------------------
## get parcel data
## ------------------------------------------

## Charlottesville neighborhoods in geojson
url <- paste0(base_url, '0e9946c2a77d4fc6ad16d9968509c588_72.geojson')

## read data
parcel <- st_read(url) %>%
    ## lower names
    rename_all(tolower)

## ------------------------------------------
## get residential detail
## ------------------------------------------

res <- read_csv(file.path(ddir,
                          'addresses-joined-to-details-residential-with-lat-lon.csv'))

## ------------------------------------------
## get commerical detail
## ------------------------------------------

com <- read_csv(file.path(ddir,
                          'addresses-joined-to-details-commercial-with-lat-lon.csv'))

## ------------------------------------------
## get fire data
## ------------------------------------------

fire <- st_read(file.path(ddir, 'HISTORICAL_FIRE.geojson'))


## ------------------------------------------
## join
## ------------------------------------------

df <- st_join(parcel, fire) %>%
    left_join(res, by = c('pin' = 'parcel_number')) %>%
    left_join(com, by = c('pin' = 'parcel_number'))

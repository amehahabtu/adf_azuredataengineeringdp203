# ADLS Key
spark.conf.set(
  'fs.azure.account.key.adlsoct.dfs.core.windows.net'
  , '4lX8p6VGIMLtSPLIuoKCBATg7fm+FzXQZPiB8VfkQA1113ep5BdEcIernYpbSavx1K9UrtxgtGWwM/ge6SYroQ=='
)


-------------------------------------------------------------------------------

# List folder in ADLS
dbutils.fs.ls('abfss://raw@adlsoct.dfs.core.windows.net')


----------------------------------------------------------------------------------

# Read file from ADLS
source_file = 'abfss://raw@adlsoct.dfs.core.windows.net/TopMovies_Part1.csv'

df = spark.read\
  .format('csv')\
  .option('inferSchema', True)\
  .option('header', True)\
  .option('delimiter', ',')\
  .load(source_file)

display(df.limit(10))
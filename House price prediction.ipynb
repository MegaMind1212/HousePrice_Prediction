{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "25cd0fce",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9c8c648b",
   "metadata": {},
   "outputs": [],
   "source": [
    "data=pd.read_csv('train.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a097511c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>beds</th>\n",
       "      <th>baths</th>\n",
       "      <th>size</th>\n",
       "      <th>size_units</th>\n",
       "      <th>lot_size</th>\n",
       "      <th>lot_size_units</th>\n",
       "      <th>zip_code</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>2.5</td>\n",
       "      <td>2590.0</td>\n",
       "      <td>sqft</td>\n",
       "      <td>6000.00</td>\n",
       "      <td>sqft</td>\n",
       "      <td>98144</td>\n",
       "      <td>795000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2240.0</td>\n",
       "      <td>sqft</td>\n",
       "      <td>0.31</td>\n",
       "      <td>acre</td>\n",
       "      <td>98106</td>\n",
       "      <td>915000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2040.0</td>\n",
       "      <td>sqft</td>\n",
       "      <td>3783.00</td>\n",
       "      <td>sqft</td>\n",
       "      <td>98107</td>\n",
       "      <td>950000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3800.0</td>\n",
       "      <td>sqft</td>\n",
       "      <td>5175.00</td>\n",
       "      <td>sqft</td>\n",
       "      <td>98199</td>\n",
       "      <td>1950000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1042.0</td>\n",
       "      <td>sqft</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>98102</td>\n",
       "      <td>950000.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   beds  baths    size size_units  lot_size lot_size_units  zip_code  \\\n",
       "0     3    2.5  2590.0       sqft   6000.00           sqft     98144   \n",
       "1     4    2.0  2240.0       sqft      0.31           acre     98106   \n",
       "2     4    3.0  2040.0       sqft   3783.00           sqft     98107   \n",
       "3     4    3.0  3800.0       sqft   5175.00           sqft     98199   \n",
       "4     2    2.0  1042.0       sqft       NaN            NaN     98102   \n",
       "\n",
       "       price  \n",
       "0   795000.0  \n",
       "1   915000.0  \n",
       "2   950000.0  \n",
       "3  1950000.0  \n",
       "4   950000.0  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7ab13fa4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2016, 8)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "58edc261",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2016 entries, 0 to 2015\n",
      "Data columns (total 8 columns):\n",
      " #   Column          Non-Null Count  Dtype  \n",
      "---  ------          --------------  -----  \n",
      " 0   beds            2016 non-null   int64  \n",
      " 1   baths           2016 non-null   float64\n",
      " 2   size            2016 non-null   float64\n",
      " 3   size_units      2016 non-null   object \n",
      " 4   lot_size        1669 non-null   float64\n",
      " 5   lot_size_units  1669 non-null   object \n",
      " 6   zip_code        2016 non-null   int64  \n",
      " 7   price           2016 non-null   float64\n",
      "dtypes: float64(4), int64(2), object(2)\n",
      "memory usage: 126.1+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "01c45103",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3     645\n",
      "2     560\n",
      "4     398\n",
      "1     256\n",
      "5     123\n",
      "6      22\n",
      "9       5\n",
      "7       3\n",
      "8       2\n",
      "15      1\n",
      "14      1\n",
      "Name: beds, dtype: int64\n",
      "********************\n",
      "2.0    627\n",
      "1.0    493\n",
      "2.5    282\n",
      "3.0    198\n",
      "3.5    179\n",
      "1.5    137\n",
      "4.0     37\n",
      "4.5     21\n",
      "5.0     16\n",
      "5.5     13\n",
      "6.0      5\n",
      "7.0      4\n",
      "8.5      1\n",
      "0.5      1\n",
      "9.0      1\n",
      "6.5      1\n",
      "Name: baths, dtype: int64\n",
      "********************\n",
      "2080.0    12\n",
      "1440.0    11\n",
      "1460.0    11\n",
      "1370.0    11\n",
      "1670.0    11\n",
      "          ..\n",
      "1548.0     1\n",
      "1174.0     1\n",
      "1865.0     1\n",
      "578.0      1\n",
      "795.0      1\n",
      "Name: size, Length: 879, dtype: int64\n",
      "********************\n",
      "sqft    2016\n",
      "Name: size_units, dtype: int64\n",
      "********************\n",
      "5000.0    61\n",
      "4000.0    45\n",
      "6000.0    38\n",
      "1.0       26\n",
      "4800.0    16\n",
      "          ..\n",
      "745.0      1\n",
      "5043.0     1\n",
      "2256.0     1\n",
      "8540.0     1\n",
      "4267.0     1\n",
      "Name: lot_size, Length: 959, dtype: int64\n",
      "********************\n",
      "sqft    1449\n",
      "acre     220\n",
      "Name: lot_size_units, dtype: int64\n",
      "********************\n",
      "98115    170\n",
      "98103    166\n",
      "98117    151\n",
      "98144    113\n",
      "98122    109\n",
      "98118    100\n",
      "98116     88\n",
      "98107     83\n",
      "98126     80\n",
      "98106     78\n",
      "98125     78\n",
      "98105     73\n",
      "98199     72\n",
      "98119     70\n",
      "98133     61\n",
      "98109     61\n",
      "98136     60\n",
      "98102     60\n",
      "98121     59\n",
      "98112     57\n",
      "98178     44\n",
      "98168     44\n",
      "98146     41\n",
      "98108     33\n",
      "98177     27\n",
      "98101     23\n",
      "98104     14\n",
      "98164      1\n",
      "Name: zip_code, dtype: int64\n",
      "********************\n",
      "750000.0     27\n",
      "700000.0     25\n",
      "850000.0     23\n",
      "950000.0     20\n",
      "900000.0     19\n",
      "             ..\n",
      "205000.0      1\n",
      "3400000.0     1\n",
      "1278500.0     1\n",
      "6250000.0     1\n",
      "659000.0      1\n",
      "Name: price, Length: 767, dtype: int64\n",
      "********************\n"
     ]
    }
   ],
   "source": [
    "for column in data.columns:\n",
    "    print(data[column].value_counts())\n",
    "    print(\"*\"*20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "86b061e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "beds                0\n",
       "baths               0\n",
       "size                0\n",
       "size_units          0\n",
       "lot_size          347\n",
       "lot_size_units    347\n",
       "zip_code            0\n",
       "price               0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "eacaa0b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.drop(columns=['lot_size','lot_size_units'],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9fbd29bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>beds</th>\n",
       "      <th>baths</th>\n",
       "      <th>size</th>\n",
       "      <th>zip_code</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>2016.000000</td>\n",
       "      <td>2016.000000</td>\n",
       "      <td>2016.000000</td>\n",
       "      <td>2016.000000</td>\n",
       "      <td>2.016000e+03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2.857639</td>\n",
       "      <td>2.159970</td>\n",
       "      <td>1735.740575</td>\n",
       "      <td>98123.638889</td>\n",
       "      <td>9.636252e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.255092</td>\n",
       "      <td>1.002023</td>\n",
       "      <td>920.132591</td>\n",
       "      <td>22.650819</td>\n",
       "      <td>9.440954e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.500000</td>\n",
       "      <td>250.000000</td>\n",
       "      <td>98101.000000</td>\n",
       "      <td>1.590000e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.500000</td>\n",
       "      <td>1068.750000</td>\n",
       "      <td>98108.000000</td>\n",
       "      <td>6.017500e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1560.000000</td>\n",
       "      <td>98117.000000</td>\n",
       "      <td>8.000000e+05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>2.500000</td>\n",
       "      <td>2222.500000</td>\n",
       "      <td>98126.000000</td>\n",
       "      <td>1.105250e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>15.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>11010.000000</td>\n",
       "      <td>98199.000000</td>\n",
       "      <td>2.500000e+07</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              beds        baths          size      zip_code         price\n",
       "count  2016.000000  2016.000000   2016.000000   2016.000000  2.016000e+03\n",
       "mean      2.857639     2.159970   1735.740575  98123.638889  9.636252e+05\n",
       "std       1.255092     1.002023    920.132591     22.650819  9.440954e+05\n",
       "min       1.000000     0.500000    250.000000  98101.000000  1.590000e+05\n",
       "25%       2.000000     1.500000   1068.750000  98108.000000  6.017500e+05\n",
       "50%       3.000000     2.000000   1560.000000  98117.000000  8.000000e+05\n",
       "75%       4.000000     2.500000   2222.500000  98126.000000  1.105250e+06\n",
       "max      15.000000     9.000000  11010.000000  98199.000000  2.500000e+07"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "90f3f0b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2016 entries, 0 to 2015\n",
      "Data columns (total 6 columns):\n",
      " #   Column      Non-Null Count  Dtype  \n",
      "---  ------      --------------  -----  \n",
      " 0   beds        2016 non-null   int64  \n",
      " 1   baths       2016 non-null   float64\n",
      " 2   size        2016 non-null   float64\n",
      " 3   size_units  2016 non-null   object \n",
      " 4   zip_code    2016 non-null   int64  \n",
      " 5   price       2016 non-null   float64\n",
      "dtypes: float64(3), int64(2), object(1)\n",
      "memory usage: 94.6+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "26f2367f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3     645\n",
       "2     560\n",
       "4     398\n",
       "1     256\n",
       "5     123\n",
       "6      22\n",
       "9       5\n",
       "7       3\n",
       "8       2\n",
       "15      1\n",
       "14      1\n",
       "Name: beds, dtype: int64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['beds'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "521b9b92",
   "metadata": {},
   "source": [
    "we do not have columns with missing values anymore so we dont need to replace any null values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "aa791f84",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>beds</th>\n",
       "      <th>baths</th>\n",
       "      <th>size</th>\n",
       "      <th>zip_code</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>2.5</td>\n",
       "      <td>2590.0</td>\n",
       "      <td>98144</td>\n",
       "      <td>795000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2240.0</td>\n",
       "      <td>98106</td>\n",
       "      <td>915000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2040.0</td>\n",
       "      <td>98107</td>\n",
       "      <td>950000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3800.0</td>\n",
       "      <td>98199</td>\n",
       "      <td>1950000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1042.0</td>\n",
       "      <td>98102</td>\n",
       "      <td>950000.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   beds  baths    size  zip_code      price\n",
       "0     3    2.5  2590.0     98144   795000.0\n",
       "1     4    2.0  2240.0     98106   915000.0\n",
       "2     4    3.0  2040.0     98107   950000.0\n",
       "3     4    3.0  3800.0     98199  1950000.0\n",
       "4     2    2.0  1042.0     98102   950000.0"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "922c05a2",
   "metadata": {},
   "source": [
    "# Price per sq feet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "cc7484be",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['price_per_sqft'] = data['price'] * 100000 / data['size']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "d43ada2d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       3.069498e+07\n",
       "1       4.084821e+07\n",
       "2       4.656863e+07\n",
       "3       5.131579e+07\n",
       "4       9.117083e+07\n",
       "            ...     \n",
       "2011    6.642336e+07\n",
       "2012    6.186727e+07\n",
       "2013    5.373832e+07\n",
       "2014    7.421384e+07\n",
       "2015    3.853801e+07\n",
       "Name: price_per_sqft, Length: 2016, dtype: float64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['price_per_sqft']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "ed421be3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>beds</th>\n",
       "      <th>baths</th>\n",
       "      <th>size</th>\n",
       "      <th>zip_code</th>\n",
       "      <th>price</th>\n",
       "      <th>price_per_sqft</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>2016.000000</td>\n",
       "      <td>2016.000000</td>\n",
       "      <td>2016.000000</td>\n",
       "      <td>2016.000000</td>\n",
       "      <td>2.016000e+03</td>\n",
       "      <td>2.016000e+03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2.857639</td>\n",
       "      <td>2.159970</td>\n",
       "      <td>1735.740575</td>\n",
       "      <td>98123.638889</td>\n",
       "      <td>9.636252e+05</td>\n",
       "      <td>5.915851e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.255092</td>\n",
       "      <td>1.002023</td>\n",
       "      <td>920.132591</td>\n",
       "      <td>22.650819</td>\n",
       "      <td>9.440954e+05</td>\n",
       "      <td>8.327952e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.500000</td>\n",
       "      <td>250.000000</td>\n",
       "      <td>98101.000000</td>\n",
       "      <td>1.590000e+05</td>\n",
       "      <td>6.796117e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.500000</td>\n",
       "      <td>1068.750000</td>\n",
       "      <td>98108.000000</td>\n",
       "      <td>6.017500e+05</td>\n",
       "      <td>4.452221e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1560.000000</td>\n",
       "      <td>98117.000000</td>\n",
       "      <td>8.000000e+05</td>\n",
       "      <td>5.529762e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>2.500000</td>\n",
       "      <td>2222.500000</td>\n",
       "      <td>98126.000000</td>\n",
       "      <td>1.105250e+06</td>\n",
       "      <td>6.595389e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>15.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>11010.000000</td>\n",
       "      <td>98199.000000</td>\n",
       "      <td>2.500000e+07</td>\n",
       "      <td>3.424658e+09</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              beds        baths          size      zip_code         price  \\\n",
       "count  2016.000000  2016.000000   2016.000000   2016.000000  2.016000e+03   \n",
       "mean      2.857639     2.159970   1735.740575  98123.638889  9.636252e+05   \n",
       "std       1.255092     1.002023    920.132591     22.650819  9.440954e+05   \n",
       "min       1.000000     0.500000    250.000000  98101.000000  1.590000e+05   \n",
       "25%       2.000000     1.500000   1068.750000  98108.000000  6.017500e+05   \n",
       "50%       3.000000     2.000000   1560.000000  98117.000000  8.000000e+05   \n",
       "75%       4.000000     2.500000   2222.500000  98126.000000  1.105250e+06   \n",
       "max      15.000000     9.000000  11010.000000  98199.000000  2.500000e+07   \n",
       "\n",
       "       price_per_sqft  \n",
       "count    2.016000e+03  \n",
       "mean     5.915851e+07  \n",
       "std      8.327952e+07  \n",
       "min      6.796117e+06  \n",
       "25%      4.452221e+07  \n",
       "50%      5.529762e+07  \n",
       "75%      6.595389e+07  \n",
       "max      3.424658e+09  "
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "f6ab006e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2016, 6)"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "7a54443c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>beds</th>\n",
       "      <th>baths</th>\n",
       "      <th>size</th>\n",
       "      <th>zip_code</th>\n",
       "      <th>price</th>\n",
       "      <th>price_per_sqft</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>2.5</td>\n",
       "      <td>2590.0</td>\n",
       "      <td>98144</td>\n",
       "      <td>795000.0</td>\n",
       "      <td>3.069498e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2240.0</td>\n",
       "      <td>98106</td>\n",
       "      <td>915000.0</td>\n",
       "      <td>4.084821e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2040.0</td>\n",
       "      <td>98107</td>\n",
       "      <td>950000.0</td>\n",
       "      <td>4.656863e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3800.0</td>\n",
       "      <td>98199</td>\n",
       "      <td>1950000.0</td>\n",
       "      <td>5.131579e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1042.0</td>\n",
       "      <td>98102</td>\n",
       "      <td>950000.0</td>\n",
       "      <td>9.117083e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2011</th>\n",
       "      <td>3</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1370.0</td>\n",
       "      <td>98112</td>\n",
       "      <td>910000.0</td>\n",
       "      <td>6.642336e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012</th>\n",
       "      <td>1</td>\n",
       "      <td>1.0</td>\n",
       "      <td>889.0</td>\n",
       "      <td>98121</td>\n",
       "      <td>550000.0</td>\n",
       "      <td>6.186727e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2013</th>\n",
       "      <td>4</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2140.0</td>\n",
       "      <td>98199</td>\n",
       "      <td>1150000.0</td>\n",
       "      <td>5.373832e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014</th>\n",
       "      <td>2</td>\n",
       "      <td>2.0</td>\n",
       "      <td>795.0</td>\n",
       "      <td>98103</td>\n",
       "      <td>590000.0</td>\n",
       "      <td>7.421384e+07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015</th>\n",
       "      <td>3</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1710.0</td>\n",
       "      <td>98133</td>\n",
       "      <td>659000.0</td>\n",
       "      <td>3.853801e+07</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2016 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      beds  baths    size  zip_code      price  price_per_sqft\n",
       "0        3    2.5  2590.0     98144   795000.0    3.069498e+07\n",
       "1        4    2.0  2240.0     98106   915000.0    4.084821e+07\n",
       "2        4    3.0  2040.0     98107   950000.0    4.656863e+07\n",
       "3        4    3.0  3800.0     98199  1950000.0    5.131579e+07\n",
       "4        2    2.0  1042.0     98102   950000.0    9.117083e+07\n",
       "...    ...    ...     ...       ...        ...             ...\n",
       "2011     3    2.0  1370.0     98112   910000.0    6.642336e+07\n",
       "2012     1    1.0   889.0     98121   550000.0    6.186727e+07\n",
       "2013     4    2.0  2140.0     98199  1150000.0    5.373832e+07\n",
       "2014     2    2.0   795.0     98103   590000.0    7.421384e+07\n",
       "2015     3    2.0  1710.0     98133   659000.0    3.853801e+07\n",
       "\n",
       "[2016 rows x 6 columns]"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "d84aee8a",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "\"['size_units'] not found in axis\"",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Input \u001b[1;32mIn [39]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mdata\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdrop\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcolumns\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43msize_units\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\u001b[43minplace\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mTrue\u001b[39;49;00m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pandas\\util\\_decorators.py:311\u001b[0m, in \u001b[0;36mdeprecate_nonkeyword_arguments.<locals>.decorate.<locals>.wrapper\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    305\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(args) \u001b[38;5;241m>\u001b[39m num_allow_args:\n\u001b[0;32m    306\u001b[0m     warnings\u001b[38;5;241m.\u001b[39mwarn(\n\u001b[0;32m    307\u001b[0m         msg\u001b[38;5;241m.\u001b[39mformat(arguments\u001b[38;5;241m=\u001b[39marguments),\n\u001b[0;32m    308\u001b[0m         \u001b[38;5;167;01mFutureWarning\u001b[39;00m,\n\u001b[0;32m    309\u001b[0m         stacklevel\u001b[38;5;241m=\u001b[39mstacklevel,\n\u001b[0;32m    310\u001b[0m     )\n\u001b[1;32m--> 311\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m func(\u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "File \u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pandas\\core\\frame.py:4954\u001b[0m, in \u001b[0;36mDataFrame.drop\u001b[1;34m(self, labels, axis, index, columns, level, inplace, errors)\u001b[0m\n\u001b[0;32m   4806\u001b[0m \u001b[38;5;129m@deprecate_nonkeyword_arguments\u001b[39m(version\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m, allowed_args\u001b[38;5;241m=\u001b[39m[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mself\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlabels\u001b[39m\u001b[38;5;124m\"\u001b[39m])\n\u001b[0;32m   4807\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mdrop\u001b[39m(\n\u001b[0;32m   4808\u001b[0m     \u001b[38;5;28mself\u001b[39m,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   4815\u001b[0m     errors: \u001b[38;5;28mstr\u001b[39m \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraise\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   4816\u001b[0m ):\n\u001b[0;32m   4817\u001b[0m     \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m   4818\u001b[0m \u001b[38;5;124;03m    Drop specified labels from rows or columns.\u001b[39;00m\n\u001b[0;32m   4819\u001b[0m \n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   4952\u001b[0m \u001b[38;5;124;03m            weight  1.0     0.8\u001b[39;00m\n\u001b[0;32m   4953\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m-> 4954\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43msuper\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdrop\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m   4955\u001b[0m \u001b[43m        \u001b[49m\u001b[43mlabels\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mlabels\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   4956\u001b[0m \u001b[43m        \u001b[49m\u001b[43maxis\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   4957\u001b[0m \u001b[43m        \u001b[49m\u001b[43mindex\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mindex\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   4958\u001b[0m \u001b[43m        \u001b[49m\u001b[43mcolumns\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mcolumns\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   4959\u001b[0m \u001b[43m        \u001b[49m\u001b[43mlevel\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mlevel\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   4960\u001b[0m \u001b[43m        \u001b[49m\u001b[43minplace\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43minplace\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   4961\u001b[0m \u001b[43m        \u001b[49m\u001b[43merrors\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   4962\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pandas\\core\\generic.py:4267\u001b[0m, in \u001b[0;36mNDFrame.drop\u001b[1;34m(self, labels, axis, index, columns, level, inplace, errors)\u001b[0m\n\u001b[0;32m   4265\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m axis, labels \u001b[38;5;129;01min\u001b[39;00m axes\u001b[38;5;241m.\u001b[39mitems():\n\u001b[0;32m   4266\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m labels \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m-> 4267\u001b[0m         obj \u001b[38;5;241m=\u001b[39m \u001b[43mobj\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_drop_axis\u001b[49m\u001b[43m(\u001b[49m\u001b[43mlabels\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mlevel\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mlevel\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43merrors\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43merrors\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   4269\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m inplace:\n\u001b[0;32m   4270\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_update_inplace(obj)\n",
      "File \u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pandas\\core\\generic.py:4311\u001b[0m, in \u001b[0;36mNDFrame._drop_axis\u001b[1;34m(self, labels, axis, level, errors, consolidate, only_slice)\u001b[0m\n\u001b[0;32m   4309\u001b[0m         new_axis \u001b[38;5;241m=\u001b[39m axis\u001b[38;5;241m.\u001b[39mdrop(labels, level\u001b[38;5;241m=\u001b[39mlevel, errors\u001b[38;5;241m=\u001b[39merrors)\n\u001b[0;32m   4310\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m-> 4311\u001b[0m         new_axis \u001b[38;5;241m=\u001b[39m \u001b[43maxis\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdrop\u001b[49m\u001b[43m(\u001b[49m\u001b[43mlabels\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43merrors\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43merrors\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   4312\u001b[0m     indexer \u001b[38;5;241m=\u001b[39m axis\u001b[38;5;241m.\u001b[39mget_indexer(new_axis)\n\u001b[0;32m   4314\u001b[0m \u001b[38;5;66;03m# Case for non-unique axis\u001b[39;00m\n\u001b[0;32m   4315\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n",
      "File \u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pandas\\core\\indexes\\base.py:6644\u001b[0m, in \u001b[0;36mIndex.drop\u001b[1;34m(self, labels, errors)\u001b[0m\n\u001b[0;32m   6642\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m mask\u001b[38;5;241m.\u001b[39many():\n\u001b[0;32m   6643\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m errors \u001b[38;5;241m!=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mignore\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[1;32m-> 6644\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mlist\u001b[39m(labels[mask])\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m not found in axis\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m   6645\u001b[0m     indexer \u001b[38;5;241m=\u001b[39m indexer[\u001b[38;5;241m~\u001b[39mmask]\n\u001b[0;32m   6646\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdelete(indexer)\n",
      "\u001b[1;31mKeyError\u001b[0m: \"['size_units'] not found in axis\""
     ]
    }
   ],
   "source": [
    "data.drop(columns=['size_units'],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "95b4e3eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.drop(columns=['price_per_sqft'],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4f62d83",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aea3d617",
   "metadata": {},
   "source": [
    "saving final dataset to be used"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31c40ebf",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.to_csv(\"final_dataset.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "40ca0db3",
   "metadata": {},
   "outputs": [],
   "source": [
    "X=data.drop(columns=['price'])\n",
    "y=data['price']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01c42c3f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression,Lasso,Ridge\n",
    "from sklearn.preprocessing import OneHotEncoder, StandardScaler\n",
    "from sklearn.compose import make_column_transformer\n",
    "from sklearn.pipeline import make_pipeline\n",
    "from sklearn.metrics import r2_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "8a740178",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "1f2efa43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1612, 4)\n",
      "(1612,)\n"
     ]
    }
   ],
   "source": [
    "print(X_train.shape)\n",
    "print(y_train.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4b80e7c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "2fed0c8b",
   "metadata": {},
   "source": [
    "# Applying Linear Regression\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "d9d205a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "column_trans = make_column_transformer((OneHotEncoder(sparse=False), ['beds']), remainder='passthrough')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "57e763de",
   "metadata": {},
   "outputs": [],
   "source": [
    "scaler = StandardScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "da543673",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "__init__() got an unexpected keyword argument 'normalize'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [45]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m lr \u001b[38;5;241m=\u001b[39m \u001b[43mLinearRegression\u001b[49m\u001b[43m(\u001b[49m\u001b[43mnormalize\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mTrue\u001b[39;49;00m\u001b[43m)\u001b[49m\n",
      "\u001b[1;31mTypeError\u001b[0m: __init__() got an unexpected keyword argument 'normalize'"
     ]
    }
   ],
   "source": [
    "lr = LinearRegression(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "532ff6c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "lr = LinearRegression()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "136ba9f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "# X being feature matrix\n",
    "scaler = StandardScaler()\n",
    "X_scaled = scaler.fit_transform(X)\n",
    "\n",
    "lr = LinearRegression()\n",
    "lr.fit(X_scaled, y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "21083a35",
   "metadata": {},
   "outputs": [],
   "source": [
    "pipe = make_pipeline(column_trans,scaler, lr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "275d9d85",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\preprocessing\\_encoders.py:972: FutureWarning: `sparse` was renamed to `sparse_output` in version 1.2 and will be removed in 1.4. `sparse_output` is ignored unless you leave `sparse` to its default value.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-2 {color: black;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>Pipeline(steps=[(&#x27;columntransformer&#x27;,\n",
       "                 ColumnTransformer(remainder=&#x27;passthrough&#x27;,\n",
       "                                   transformers=[(&#x27;onehotencoder&#x27;,\n",
       "                                                  OneHotEncoder(sparse=False),\n",
       "                                                  [&#x27;beds&#x27;])])),\n",
       "                (&#x27;standardscaler&#x27;, StandardScaler()),\n",
       "                (&#x27;linearregression&#x27;, LinearRegression())])</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" ><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">Pipeline</label><div class=\"sk-toggleable__content\"><pre>Pipeline(steps=[(&#x27;columntransformer&#x27;,\n",
       "                 ColumnTransformer(remainder=&#x27;passthrough&#x27;,\n",
       "                                   transformers=[(&#x27;onehotencoder&#x27;,\n",
       "                                                  OneHotEncoder(sparse=False),\n",
       "                                                  [&#x27;beds&#x27;])])),\n",
       "                (&#x27;standardscaler&#x27;, StandardScaler()),\n",
       "                (&#x27;linearregression&#x27;, LinearRegression())])</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" ><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">columntransformer: ColumnTransformer</label><div class=\"sk-toggleable__content\"><pre>ColumnTransformer(remainder=&#x27;passthrough&#x27;,\n",
       "                  transformers=[(&#x27;onehotencoder&#x27;, OneHotEncoder(sparse=False),\n",
       "                                 [&#x27;beds&#x27;])])</pre></div></div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-4\" type=\"checkbox\" ><label for=\"sk-estimator-id-4\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">onehotencoder</label><div class=\"sk-toggleable__content\"><pre>[&#x27;beds&#x27;]</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-5\" type=\"checkbox\" ><label for=\"sk-estimator-id-5\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">OneHotEncoder</label><div class=\"sk-toggleable__content\"><pre>OneHotEncoder(sparse=False)</pre></div></div></div></div></div></div><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-6\" type=\"checkbox\" ><label for=\"sk-estimator-id-6\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">remainder</label><div class=\"sk-toggleable__content\"><pre>[&#x27;baths&#x27;, &#x27;size&#x27;, &#x27;zip_code&#x27;]</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-7\" type=\"checkbox\" ><label for=\"sk-estimator-id-7\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">passthrough</label><div class=\"sk-toggleable__content\"><pre>passthrough</pre></div></div></div></div></div></div></div></div><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-8\" type=\"checkbox\" ><label for=\"sk-estimator-id-8\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">StandardScaler</label><div class=\"sk-toggleable__content\"><pre>StandardScaler()</pre></div></div></div><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-9\" type=\"checkbox\" ><label for=\"sk-estimator-id-9\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "Pipeline(steps=[('columntransformer',\n",
       "                 ColumnTransformer(remainder='passthrough',\n",
       "                                   transformers=[('onehotencoder',\n",
       "                                                  OneHotEncoder(sparse=False),\n",
       "                                                  ['beds'])])),\n",
       "                ('standardscaler', StandardScaler()),\n",
       "                ('linearregression', LinearRegression())])"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pipe.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "99decaf5",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred_lr = pipe.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "9d619c2d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5728152391843129"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r2_score(y_test,y_pred_lr)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7f0ca365",
   "metadata": {},
   "source": [
    "# using lasso"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "8311eaa5",
   "metadata": {},
   "outputs": [],
   "source": [
    "lasso = Lasso()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "02cba156",
   "metadata": {},
   "outputs": [],
   "source": [
    "pipe = make_pipeline(column_trans,scaler, lasso)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "f252f723",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\preprocessing\\_encoders.py:972: FutureWarning: `sparse` was renamed to `sparse_output` in version 1.2 and will be removed in 1.4. `sparse_output` is ignored unless you leave `sparse` to its default value.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-3 {color: black;}#sk-container-id-3 pre{padding: 0;}#sk-container-id-3 div.sk-toggleable {background-color: white;}#sk-container-id-3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-3 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-3 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-3 div.sk-item {position: relative;z-index: 1;}#sk-container-id-3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-3 div.sk-item::before, #sk-container-id-3 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-3 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-3 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-3 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-3 div.sk-label-container {text-align: center;}#sk-container-id-3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-3 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-3\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>Pipeline(steps=[(&#x27;columntransformer&#x27;,\n",
       "                 ColumnTransformer(remainder=&#x27;passthrough&#x27;,\n",
       "                                   transformers=[(&#x27;onehotencoder&#x27;,\n",
       "                                                  OneHotEncoder(sparse=False),\n",
       "                                                  [&#x27;beds&#x27;])])),\n",
       "                (&#x27;standardscaler&#x27;, StandardScaler()), (&#x27;lasso&#x27;, Lasso())])</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-10\" type=\"checkbox\" ><label for=\"sk-estimator-id-10\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">Pipeline</label><div class=\"sk-toggleable__content\"><pre>Pipeline(steps=[(&#x27;columntransformer&#x27;,\n",
       "                 ColumnTransformer(remainder=&#x27;passthrough&#x27;,\n",
       "                                   transformers=[(&#x27;onehotencoder&#x27;,\n",
       "                                                  OneHotEncoder(sparse=False),\n",
       "                                                  [&#x27;beds&#x27;])])),\n",
       "                (&#x27;standardscaler&#x27;, StandardScaler()), (&#x27;lasso&#x27;, Lasso())])</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-11\" type=\"checkbox\" ><label for=\"sk-estimator-id-11\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">columntransformer: ColumnTransformer</label><div class=\"sk-toggleable__content\"><pre>ColumnTransformer(remainder=&#x27;passthrough&#x27;,\n",
       "                  transformers=[(&#x27;onehotencoder&#x27;, OneHotEncoder(sparse=False),\n",
       "                                 [&#x27;beds&#x27;])])</pre></div></div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-12\" type=\"checkbox\" ><label for=\"sk-estimator-id-12\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">onehotencoder</label><div class=\"sk-toggleable__content\"><pre>[&#x27;beds&#x27;]</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-13\" type=\"checkbox\" ><label for=\"sk-estimator-id-13\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">OneHotEncoder</label><div class=\"sk-toggleable__content\"><pre>OneHotEncoder(sparse=False)</pre></div></div></div></div></div></div><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-14\" type=\"checkbox\" ><label for=\"sk-estimator-id-14\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">remainder</label><div class=\"sk-toggleable__content\"><pre>[&#x27;baths&#x27;, &#x27;size&#x27;, &#x27;zip_code&#x27;]</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-15\" type=\"checkbox\" ><label for=\"sk-estimator-id-15\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">passthrough</label><div class=\"sk-toggleable__content\"><pre>passthrough</pre></div></div></div></div></div></div></div></div><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-16\" type=\"checkbox\" ><label for=\"sk-estimator-id-16\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">StandardScaler</label><div class=\"sk-toggleable__content\"><pre>StandardScaler()</pre></div></div></div><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-17\" type=\"checkbox\" ><label for=\"sk-estimator-id-17\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">Lasso</label><div class=\"sk-toggleable__content\"><pre>Lasso()</pre></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "Pipeline(steps=[('columntransformer',\n",
       "                 ColumnTransformer(remainder='passthrough',\n",
       "                                   transformers=[('onehotencoder',\n",
       "                                                  OneHotEncoder(sparse=False),\n",
       "                                                  ['beds'])])),\n",
       "                ('standardscaler', StandardScaler()), ('lasso', Lasso())])"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pipe.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "d0909214",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5746817917322382"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred_lasso = pipe.predict(X_test)\n",
    "r2_score(y_test,y_pred_lasso)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f319cc4",
   "metadata": {},
   "source": [
    "# using Ridge"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "fb318f91",
   "metadata": {},
   "outputs": [],
   "source": [
    "ridge = Ridge()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "ace346e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "pipe = make_pipeline(column_trans,scaler, ridge)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "9358a569",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\preprocessing\\_encoders.py:972: FutureWarning: `sparse` was renamed to `sparse_output` in version 1.2 and will be removed in 1.4. `sparse_output` is ignored unless you leave `sparse` to its default value.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-4 {color: black;}#sk-container-id-4 pre{padding: 0;}#sk-container-id-4 div.sk-toggleable {background-color: white;}#sk-container-id-4 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-4 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-4 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-4 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-4 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-4 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-4 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-4 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-4 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-4 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-4 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-4 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-4 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-4 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-4 div.sk-item {position: relative;z-index: 1;}#sk-container-id-4 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-4 div.sk-item::before, #sk-container-id-4 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-4 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-4 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-4 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-4 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-4 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-4 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-4 div.sk-label-container {text-align: center;}#sk-container-id-4 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-4 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-4\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>Pipeline(steps=[(&#x27;columntransformer&#x27;,\n",
       "                 ColumnTransformer(remainder=&#x27;passthrough&#x27;,\n",
       "                                   transformers=[(&#x27;onehotencoder&#x27;,\n",
       "                                                  OneHotEncoder(sparse=False),\n",
       "                                                  [&#x27;beds&#x27;])])),\n",
       "                (&#x27;standardscaler&#x27;, StandardScaler()), (&#x27;ridge&#x27;, Ridge())])</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-18\" type=\"checkbox\" ><label for=\"sk-estimator-id-18\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">Pipeline</label><div class=\"sk-toggleable__content\"><pre>Pipeline(steps=[(&#x27;columntransformer&#x27;,\n",
       "                 ColumnTransformer(remainder=&#x27;passthrough&#x27;,\n",
       "                                   transformers=[(&#x27;onehotencoder&#x27;,\n",
       "                                                  OneHotEncoder(sparse=False),\n",
       "                                                  [&#x27;beds&#x27;])])),\n",
       "                (&#x27;standardscaler&#x27;, StandardScaler()), (&#x27;ridge&#x27;, Ridge())])</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-19\" type=\"checkbox\" ><label for=\"sk-estimator-id-19\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">columntransformer: ColumnTransformer</label><div class=\"sk-toggleable__content\"><pre>ColumnTransformer(remainder=&#x27;passthrough&#x27;,\n",
       "                  transformers=[(&#x27;onehotencoder&#x27;, OneHotEncoder(sparse=False),\n",
       "                                 [&#x27;beds&#x27;])])</pre></div></div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-20\" type=\"checkbox\" ><label for=\"sk-estimator-id-20\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">onehotencoder</label><div class=\"sk-toggleable__content\"><pre>[&#x27;beds&#x27;]</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-21\" type=\"checkbox\" ><label for=\"sk-estimator-id-21\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">OneHotEncoder</label><div class=\"sk-toggleable__content\"><pre>OneHotEncoder(sparse=False)</pre></div></div></div></div></div></div><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-22\" type=\"checkbox\" ><label for=\"sk-estimator-id-22\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">remainder</label><div class=\"sk-toggleable__content\"><pre>[&#x27;baths&#x27;, &#x27;size&#x27;, &#x27;zip_code&#x27;]</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-23\" type=\"checkbox\" ><label for=\"sk-estimator-id-23\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">passthrough</label><div class=\"sk-toggleable__content\"><pre>passthrough</pre></div></div></div></div></div></div></div></div><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-24\" type=\"checkbox\" ><label for=\"sk-estimator-id-24\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">StandardScaler</label><div class=\"sk-toggleable__content\"><pre>StandardScaler()</pre></div></div></div><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-25\" type=\"checkbox\" ><label for=\"sk-estimator-id-25\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">Ridge</label><div class=\"sk-toggleable__content\"><pre>Ridge()</pre></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "Pipeline(steps=[('columntransformer',\n",
       "                 ColumnTransformer(remainder='passthrough',\n",
       "                                   transformers=[('onehotencoder',\n",
       "                                                  OneHotEncoder(sparse=False),\n",
       "                                                  ['beds'])])),\n",
       "                ('standardscaler', StandardScaler()), ('ridge', Ridge())])"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pipe.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "8cf7dc4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5746884627878555"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred_ridge = pipe.predict(X_test)\n",
    "r2_score(y_test,y_pred_ridge)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "52c1ee1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No Regularization:  0.5728152391843129\n",
      "Lasso:  0.5746817917322382\n",
      "Ridge:  0.5746884627878555\n"
     ]
    }
   ],
   "source": [
    "print(\"No Regularization: \", r2_score(y_test,y_pred_lr))\n",
    "print(\"Lasso: \", r2_score(y_test,y_pred_lasso))\n",
    "print(\"Ridge: \", r2_score(y_test,y_pred_ridge))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f739a63d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48efbdca",
   "metadata": {},
   "outputs": [],
   "source": [
    "pickle.dump(pipe, open('RidgeModel.pkl','wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bf4447e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

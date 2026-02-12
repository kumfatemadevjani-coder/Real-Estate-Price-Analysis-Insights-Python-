import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_csv('data.csv')
# Display the first few rows of the dataset
print(df.head())
print(df.columns.tolist())
# Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df=df.drop_duplicates()
print(df.columns.tolist())

df['price'] = df['price'].astype(str).str.replace(',', '').astype(float)
df['area'] = df['area'].astype(str).str.replace(',', '').astype(int)
df['rate_per_sqft']=df['rate_per_sqft'].astype(str).str.replace(',', '').astype(int)
df['rate_per_sqft'] = df['price'] / df['area']
print(df['rate_per_sqft'])

# Catugorical Columns Cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
print(df['rera_approval'])
df['flat_type'] = df['flat_type'].str.strip().str.lower()
df=df.drop_duplicates()
print(df)
print(df.info())
#print(df.head())

# Which is the costliest flatin the dataset?
costliest_flat = df.loc[df['price'].idxmax()]
print("Costliest Flat:")
print(costliest_flat)
'''Costliest Flat:
let us write this output as a sentence
price                                1226300000.0
status                              ready to move
area                                        16500
rate_per_sqft                        74321.212121
property_type    6 BHK Apartment in DLF Camellias
locality                                Sector 42
builder_name                    Provident Capital
rera_approval                               False
bhk_count                                     6.0
socity                              DLF Camellias
company_name                                  DLF
flat_type                               apartment'''
print(f"The costliest flat in the dataset is a {costliest_flat['flat_type']} located in {costliest_flat['locality']} with a price of {costliest_flat['price']} in {costliest_flat['company_name']} company.")

#Which Locality has the highest average price?

highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()    
print("Locality with Highest Average Price:")
print(highest_avg_price_locality)

#which locality has the highest rate per sqft?
highest_rate_per_sqft_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print("Locality with Highest Rate per Sqft:")       
print(highest_rate_per_sqft_locality)

#Do ready to move properties cost more than under construction properties on average?
avg_price_ready_to_move = df[df['status'] == 'ready to move']['price'].mean()
avg_price_under_construction = df[df['status'] == 'under construction']['price'].mean()
if avg_price_ready_to_move > avg_price_under_construction:
    print("Ready to move properties cost more on average than under construction properties.")          
else:
    print("Under construction properties cost more on average than ready to move properties.")  

#Do Rera approved properties command a price premium?
avg_price_rera_approved = df[df['rera_approval'] == True]['price'].mean()
avg_price_not_rera_approved = df[df['rera_approval'] == False]['price'].mean()
if avg_price_rera_approved > avg_price_not_rera_approved:   
    print("Rera approved properties command a price premium on average.")       
else:
    print("Rera approved properties do not command a price premium on average.")

 # how does area impact price?
sns.scatterplot(x='area', y='price', data=df)
plt.show()

 # Which BHK configuration is most expensive based on rate per sqft?
avg_price_by_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean()
most_expensive_bhk = avg_price_by_bhk.idxmax()      
print(f"The most expensive BHK configuration is {most_expensive_bhk} BHK.")

#Which property type is the costliest?
avg_price_by_property_type = df.groupby('flat_type')['rate_per_sqft'].mean()
print(avg_price_by_property_type)

 # Do certain buiders price is higher?
print(df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5))
#print the name top 5
top_5_builders = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
for builder in top_5_builders.index:
    print(builder,end=', ')

 # Are larger homes more expensive on a per sqft basis? 
sns.scatterplot(x='area', y='rate_per_sqft', data=df)
plt.show()
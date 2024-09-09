# Task 1:  Identify Extreme Discount Prices
def extreme_Discounted_Prices(amazonProductData, category):
    highestPrice=float('-inf')
    lowestPrice=float('inf')
    
    for product in amazonProductData:
        if product[2].lower() == category.lower():
            discountedPrice = float(product[3])
            
            if discountedPrice > highestPrice:
                highestPrice = discountedPrice
                highestId = product[0]
            
            if discountedPrice < lowestPrice:
                lowestPrice = discountedPrice
                lowestId = product[0]
    
    return [highestId, lowestId]

# Task 2: Summarize Price Distribution 
def mean_median_meanAbsDeviation(amazonProductData, category):
    # storing the product that has rating count > 1000 in this variable
    actualPriceList = []
    for product in amazonProductData:
        # here product[2] is category
        if product[2].lower() == category.lower():
            if float(product[7]) > 1000:
                actualPriceList.append(float(product[4]))
    
    # mean
    mean = round((sum(actualPriceList) / len(actualPriceList)),4)
    
    # median
    sortedActualPrice = sorted(actualPriceList)
    
    n = len(sortedActualPrice)
    
    if n%2!=0:
        median = round((sortedActualPrice[n//2]),4)
    else:
        median = round(((sortedActualPrice[n//2 - 1] + sortedActualPrice[n//2]) / 2),4)
    
    # mean absolute deviation
    absoluteDeviation = []
    for value in actualPriceList:
        deviation = abs(value-mean)
        absoluteDeviation.append(deviation)
    
    meanAbsDeviation = round((sum(absoluteDeviation) / n),4)
    
    return [mean, median, meanAbsDeviation]
        
# Task 3: Calculate Standard Deviation of Discounted Percentages
def standard_deviation_of_discounted_percentages(amazonProductData, category):
    computersAndAccessoriesList = []
    electronicsList = []
    homeAndKitchenList = []
    homeImprovementList = []
    musicalInstrumentsList = []
    officeProductsList = []
    carAndMotorbikeList = []
    
    for product in amazonProductData: 
        if product[2] == 'Computers&Accessories':
            if 3.3 <= float(product[6]) <= 4.3:
                computersAndAccessoriesList.append(float(product[5]))
        elif product[2] == 'Electronics':
            if 3.3 <= float(product[6]) <= 4.3:
                electronicsList.append(float(product[5]))
        elif product[2] == 'Home&Kitchen':
            if 3.3 <= float(product[6]) <= 4.3:
                homeAndKitchenList.append(float(product[5]))
        elif product[2] == 'HomeImprovement':
            if 3.3 <= float(product[6]) <= 4.3:
                homeImprovementList.append(float(product[5]))
        elif product[2] == 'MusicalInstruments':
            if 3.3 <= float(product[6]) <= 4.3:
                musicalInstrumentsList.append(float(product[5]))
        elif product[2] == 'OfficeProducts':
            if 3.3 <= float(product[6]) <= 4.3:
                officeProductsList.append(float(product[5]))
        elif product[2] == 'Car&Motorbike':
            if 3.3 <= float(product[6]) <= 4.3:
                carAndMotorbikeList.append(float(product[5]))
    
    # finding standard deviation for Computers&Accessories
    meanOfomputersAndAccessories = sum(computersAndAccessoriesList) / len(computersAndAccessoriesList)
    computersAndAccessoriesListVariance = []
    for value in computersAndAccessoriesList:
        squaredDifferencesOfomputersAndAccessories = (value-meanOfomputersAndAccessories)**2
        computersAndAccessoriesListVariance.append(squaredDifferencesOfomputersAndAccessories)
    varianceComputersAndAccessories = sum(computersAndAccessoriesListVariance) / (len(computersAndAccessoriesListVariance)-1)
    standardDeviationComputersAndAccessories = round(((varianceComputersAndAccessories)**0.5),4)
    
    # finding standard deviation for Electronics
    meanOfElectronics = sum(electronicsList) / len(electronicsList)
    electronicsListVariance = []
    for value in electronicsList:
        squaredDifferencesOfElectronics = (value-meanOfElectronics)**2
        electronicsListVariance.append(squaredDifferencesOfElectronics)
    varianceElectronics = sum(electronicsListVariance) / (len(electronicsListVariance)-1)
    standardDeviationElectronics = round(((varianceElectronics)**0.5),4)
        
    # Finding standard deviation for Home&Kitchen
    meanOfHomeAndKitchen = sum(homeAndKitchenList) / len(homeAndKitchenList)
    homeAndKitchenListVariance = []
    for value in homeAndKitchenList:
        squaredDifferencesOfHomeAndKitchen = (value - meanOfHomeAndKitchen) ** 2
        homeAndKitchenListVariance.append(squaredDifferencesOfHomeAndKitchen)
    varianceHomeAndKitchen = sum(homeAndKitchenListVariance) / (len(homeAndKitchenListVariance) - 1)
    standardDeviationHomeAndKitchen = round(((varianceHomeAndKitchen) ** 0.5),4)
    
    # Finding standard deviation for HomeImprovement
    meanOfHomeImprovement = sum(homeImprovementList) / len(homeImprovementList)
    homeImprovementListVariance = []
    for value in homeImprovementList:
        squaredDifferencesOfHomeImprovement = (value - meanOfHomeImprovement) ** 2
        homeImprovementListVariance.append(squaredDifferencesOfHomeImprovement)
    varianceHomeImprovement = sum(homeImprovementListVariance) / (len(homeImprovementListVariance) - 1)
    standardDeviationHomeImprovement = round(((varianceHomeImprovement) ** 0.5),4)
    
    # Finding standard deviation for MusicalInstruments
    meanOfMusicalInstruments = sum(musicalInstrumentsList) / len(musicalInstrumentsList)
    musicalInstrumentsListVariance = []
    for value in musicalInstrumentsList:
        squaredDifferencesOfMusicalInstruments = (value - meanOfMusicalInstruments) ** 2
        musicalInstrumentsListVariance.append(squaredDifferencesOfMusicalInstruments)
    varianceMusicalInstruments = sum(musicalInstrumentsListVariance) / (len(musicalInstrumentsListVariance) - 1)
    standardDeviationMusicalInstruments = round(((varianceMusicalInstruments) ** 0.5),4)
    
    # Finding standard deviation for OfficeProducts
    meanOfOfficeProducts = sum(officeProductsList) / len(officeProductsList)
    officeProductsListVariance = []
    for value in officeProductsList:
        squaredDifferencesOfOfficeProducts = (value - meanOfOfficeProducts) ** 2
        officeProductsListVariance.append(squaredDifferencesOfOfficeProducts)
    varianceOfficeProducts = sum(officeProductsListVariance) / (len(officeProductsListVariance) - 1)
    standardDeviationOfficeProducts = round(((varianceOfficeProducts) ** 0.5),4)
    
    # Finding standard deviation for Car & Motorbike
    meanOfCarAndMotorbike = sum(carAndMotorbikeList) / len(carAndMotorbikeList)
    carAndMotorbikeListVariance = []
    for value in carAndMotorbikeList:
        squaredDifferencesOfCarAndMotorbike = (value - meanOfCarAndMotorbike) ** 2
        carAndMotorbikeListVariance.append(squaredDifferencesOfCarAndMotorbike)
    varianceCarAndMotorbike = sum(carAndMotorbikeListVariance) / (len(carAndMotorbikeListVariance) - 1)
    standardDeviationCarAndMotorbike = round(((varianceCarAndMotorbike) ** 0.5),4)
    
    return sorted([standardDeviationComputersAndAccessories, standardDeviationElectronics, standardDeviationHomeAndKitchen, standardDeviationHomeImprovement, standardDeviationMusicalInstruments, standardDeviationOfficeProducts, standardDeviationCarAndMotorbike],reverse=True)

# Task 4: Correlate Sales Data
def correlate_Sales_Data(productId, amazonSalesData):
    highestDiscountedPrice = productId[0].lower()
    lowestDiscountedPrice = productId[1].lower()
    
    #Emppty list for sales data
    highest_discounted_product_sales = []
    lowest_discounted_product_sales=[]
    
    for yearData in amazonSalesData:
        yearSales = {}
        
        for  i in range(1, len(yearData),2):
            productId = yearData[i-1].strip(':').lower()
            sales = int(yearData[i].strip(','))            
            yearSales[productId] = sales
       
        highest_discounted_product_sales.append(yearSales.get(highestDiscountedPrice, 0))
        lowest_discounted_product_sales.append(yearSales.get(lowestDiscountedPrice, 0))
                
    #calculate correlation
    n = len(highest_discounted_product_sales)
    sum_highest_sales = sum(highest_discounted_product_sales)
    sum_lowest_sales = sum(lowest_discounted_product_sales)
    sum_highes_lowest_sales = sum(highest_discounted_product_sales[i] * lowest_discounted_product_sales[i] for i in range(n))
    sum_highest_sales_squared = sum(highest_discounted_product_sales[i] ** 2 for i in range(n))
    sum_lowest_sales_squared = sum(lowest_discounted_product_sales[i] ** 2 for i in range(n))
        
    # Calculate the numerator and denominator for correlation formula
    numerator = n * sum_highes_lowest_sales - sum_highest_sales * sum_lowest_sales
    denominator = ((n * sum_highest_sales_squared - sum_highest_sales ** 2) * (n * sum_lowest_sales_squared - sum_lowest_sales ** 2)) ** 0.5
        
    if denominator == 0:
        return 0
    return round((numerator / denominator),4)
    
    
def main(CSVfile, TXTfile, category):
    # Reading amazon csv file
    amazonProductData = []
    with open(CSVfile, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            amazonProductData.append(values)
            
    # Reading Amazon Sales TXT file
    amazonSalesData = []
    with open(TXTfile, 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.strip().split() 
            amazonSalesData.append(values)
    
    # Task 1:  Identify Extreme Discount Prices (highest and lowest discounted price)
    productId = extreme_Discounted_Prices(amazonProductData, category)
    
    # Task 2: Summarize Price Distribution ( mean, median and mean absolute deviation)
    priceDistribution = mean_median_meanAbsDeviation(amazonProductData, category)
    
    # Task 3:  Calculate Standard Deviation of Discounted Percentages
    standardDeviation = standard_deviation_of_discounted_percentages(amazonProductData, ['Computers&Accessories','Electronics','Home&Kitchen', 'HomeImprovement', 'MusicalInstruments' ,'OfficeProducts','Car&Motorbike'])
    
    # Task 4: Correlate Sales Data
    correlationCoefficient =  correlate_Sales_Data(productId,amazonSalesData)
    
    return productId, priceDistribution, standardDeviation, correlationCoefficient

    
main('Amazon_products.csv', 'Amazon_sales.txt', 'Computers&Accessories')
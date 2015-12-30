import nltk
import textblob
from text_classify import algorithms
import pickle

def classification_sanity_checks():
    pass

def test_data():
    pass

def generate_training_data(complexity="simple"):
    """
    categories:
    * descriptive statistic:
       Show user the mean, median, mode, skew, kurtosis, counts, or some other simple description of the data
    * simple plot
       Show the user a simple plot - bar chart, pie chart, or time series
    * advanced plot
       Any other type of chart - lift chart, qq plot, etc.
    * descrete graph
       Show the user a descrete graph
    * prediction
       Given the data, predict how the data will change
    * simple query
       Return some records, based on conditions specified in the query
    * complex query
       Return some records, based on the query
    """
    if complexity == "simple":
        training_data = [
            ("What is the average number of days in this dataset?","descriptive statistic"),
            ("What are the average number of days in this dataset?","descriptive statistic"),
            ("How many cases are more than 60 days old?","descriptive statistic"),
            ("How many cases are less than 50 days old?","descriptive statistic"),
            ("What is the skew of this dataset?","descriptive statistic"),#5
            ("How many people are in this dataset?","descriptive statistic"),
            ("What is the median number of days a case has been in this dataset?","descriptive statistic"),
            ("How many days exist in this dataset, in total?","descriptive statistic"),
            ("Do men have a longer processing time than women, on average?","descriptive statistic"),
            ("How long do men have to wait to be processed on average?","descriptive statistic"), #10
            ("do men have a longer processing time than women, on average?","descriptive statistic"),
            ("how many cases are more than 150 days old?","descriptive statistic"), 
            ("What is the median number of days a case takes to be processed?","descriptive statistic"),
            ("What is the mean number of days a case takes to be processed?","descriptive statistic"),
            ("What is the mode of the number of days a case takes to be processed?","descriptive statistic"),#15
            ("What is the middle number of days a case takes to be processed?","descriptive statistic"),
            ("What is the variance of days a case takes to be processed?","descriptive statistic"),
            ("What is the standard deviation of days a case takes to be processed?","descriptive statistic"),
            ("What is the std. dev. of days a case takes to be processed?","descriptive statistic"),
            ("What is the least amount of days a case takes to be processed?","descriptive statistic"), #20
            ("average cases by days in system","descriptive statistic"),
            ("variance cases by days in system","descriptive statistic"),
            ("standard deviation by days in system","descriptive statistic"),
            ("std. dev. by days in system","descriptive statistic"),
            ("ave. cases by days in system","descriptive statistic"), #25
            ("total cases in system","descriptive statistic"),
            ("average of total cases longer than 60 days in system","descriptive statistic"),
            ("mode of total cases","descriptive statistic"),
            ("median of total cases","descriptive statistic"),
            ("all cases over 20 days","descriptive statistic"),#30 - end descriptive statistic
            ("Show me a bar chart of the total number of days a case has been here","simple plot"),
            ("Show me a bar chart of the number of days a case has been in the system","simple plot"),
            ("Show me a bar chart of the cases by amount of time they've taken","simple plot"),
            ("bar chart cases by amount of time","simple plot"),
            ("Visually explain the number of cases in the system","simple plot"),#35
            ("Plot of the number of cases that have been in the system longer than 40 days","simple plot"),
            ("Plot the number of cases that have been in the system since 2012","simple plot"),
            ("Plot the number of cases that are older than 20 days","simple plot"),
            ("Plot the number of cases that are less than 50 days","simple plot"),
            ("Make a scatter plot of the total number of cases older than 50 days","simple plot"), #40
            ("Make a pie plot of the number of cases","simple plot"),
            ("Make a bar chart of the number of cases","simple plot"),
            ("Make a pie chart of the number of cases","simple plot"),
            ("Make a time series of the number of cases","simple plot"),
            ("Make a plot of all cases over time","simple plot") #45
        ]
    pickle.dump(training_data, open("training_data.pickle","w"))
    #return training_data

def classify_query(query):
    training_data = pickle.load(open("training_data.pickle","r"))
    cl = algorithms.svm(training_data)
    classification = cl.classify(algorithms.preprocess(query))
    #To do add classification_sanity_check
    return classification
    
if __name__ == '__main__':
    generate_training_data()
    print classify_query("What is the average number of days per case?")

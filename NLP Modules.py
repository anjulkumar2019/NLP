import pandas as pd

class NLP_MODULE:
    def __init__(self, stopword , spec_character):
        self.stopword       = stopword
        self.spec_character =  spec_character
        print(self.stopword)
    
    def openfile(self, name):
        try:
            print(name)
            text_data = pd.read_excel(name)
            return(text_data)
        except:
            print('File open error')
            return(-1)
    
    def remove_spec_character(self, string):
        return_string = ""
        count=0
        for word in range(len(string)):
            if string[word] in self.spec_character:
                continue
            else:
                return_string= return_string + str(string[word])
                count=count+1
        return_string.replace("<br /><br />", " ")
        return(return_string)
    
    def remove_stopwords(self, string):
        return_string = ""
        ls = string.split(' ')
        print(ls)
        return_string = [w for w in ls if not w in self.stopword]
        return(str(return_string))
    
    def word_freq_count(self, name):
        dictionary = {}
        string_into_list = []
        data_into_string = " "
        for index, data in name.iterrows():
            data_into_string = self.remove_stopwords(self.remove_spec_character(str(data.values)))
            string_into_list = data_into_string.split(' ')
            for word in string_into_list:
                if word in dictionary:
                    count = dictionary[word] + 1
                    dictionary[word] = count
                else:
                    dictionary[word] = 1
            
        return(dictionary)
        
def main():
    remove_alphabets = ["!","@","-",".",";",":","]","[","*","(",")","/"]
    stopword = ["The", "THE", "MY","My" , "it", "to", "OK","ok","Ok","a","be", "for" , "is", ""]
    nlp = NLP_MODULE(stopword,remove_alphabets)
    file_name = 'sample_us.xlsx'
    text_data=nlp.openfile(file_name)
    word_list=nlp.word_freq_count(text_data[['review_body']])

if __name__ == '__main__':
    main()

    
        
        



    
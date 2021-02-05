import pyttsx3 #narrator voice
import sys #EXIT()
import speech_recognition as sr

r=sr.Recognizer()
r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()
r4=sr.Recognizer()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

class library:
    

    def __init__(self, list, name):

        self.book_list = list
        self.name = name
        self.lend_dict = {}

    def display_books(self):
        print(f"{self.name} LIBRARY HAS:\n ")
        for books in self.book_list:
            print(books)
        engine.say("If You Didnt get your Book Please Let us know We will soon add it to our Stock")
        engine.runAndWait()
        print("\nNOTE: If Your Book Is Not Available It Will be made Available Wihin 2 Days !")
        engine.say("Kindly Tell the Library owner If you Didnt Found Your Book !")    
        engine.runAndWait()

    def lend_book(self, user, book):

        if book not in self.lend_dict.keys():
            self.lend_dict.update({book: user})
            print('Database updated Successfully ! You can now lend this Book :)')
            engine.say("Database updated Successfully ! You can now lend this Book")
            engine.runAndWait()
            print("NOTE : Kindly Return Within 2 Weeks Otherwise you will be fined ")
            engine.say("Kindly Return Within 2 Weeks Otherwise you will be fined ")
            engine.runAndWait()

        else:
            print(f"Oh sorry ! This Book is already lend to {self.lend_dict[book]}.")
            engine.say("Oh sorry ! This Book is already lend ")
            engine.runAndWait()
            print("Dont afraid ! You can Go to E book Section To purchase the same book @100/- Or wait somedays")
            engine.say("Dont afraid ! You can go to E book section and purchase the same book at lesser cost or, wait for somedays")
            engine.runAndWait()

    def return_book(self, book):
        if book not in self.lend_dict.keys():
            print('Not Returnable !')
            engine.say("Sorry ! NO one has lend this book yet ")
            engine.runAndWait()
            
        else:
            self.lend_dict.pop(book)
            
            print("Book Returned Succesfully")
            engine.say("Book Returned Succesfully")
            engine.runAndWait()

    def add_book(self, book):
        
        self.book_list.append(book)
        
        print('Book added successfully.')
        engine.say('Book added successfully.')
        engine.runAndWait()


if __name__ == '__main__':
    
    engine.setProperty('rate', 150)
    print('\n\n\n\n\n')
    
    print('\t\t\t\t\t\t\t\t ******* Welcome to Library ******* \t\t\t\t\t\t\t\t\n')
    engine.say("Welcome To Bright Side Library");
    engine.say("So, How can I help you ?")
    engine.runAndWait()
    engine.say("Select Your Choice From the Menu list");
    engine.runAndWait()

    obj = library([
        'Python\t\t\t\t\t\t\t\t\tEngineering Physics\n', 
        'Let us C\t\t\t\t\t\t\t\tRD Sharma Class 10\n', 
        'Javascript & Jquery\t\t\t\t\t\tRD Sharma Class 11\n',
        'Machine Learning\t\t\t\t\t\tRD Sharma Class 12\n', 
        'Head First JAVA\t\t\t\t\t\t\tEngineering Mathematics\n',
        'HTML & CSS\t\t\t\t\t\t\t\tTogether Chemistry\n',
        'C++ By SUMITA ARORA\t\t\t\t\t\tTogether Mathematics\n',
        'Encyclopedia\t\t\t\t\t\t\tRS Aggarwal\n',
        'Begin with C#\t\t\t\t\t\t\tSL Arora\n','Aeronautical Studies\n'], 'BRIGHT SIDE')
    mic = sr.Microphone(device_index=1)        
    while True:
        with mic as source:

            
            print(" 1. Display Various Books Available \t(Say 'Show Book')\n 2. Add New Book \t\t\t\t\t\t(Say 'Add Book')\n 3. Lend a Book \t\t\t\t\t\t(Say 'Rent Book') \n 4. Return a Book \t\t\t\t\t\t(Say 'Return Book')\n 5. Exit\n")
            audio=r.listen(source,timeout=5)

        if  'show book' in r.recognize_google(audio):
            try:
                get = r.recognize_google(audio)
                
            
                obj.display_books()
            except:
                print("Unable To Undersatnd")

        elif 'add book' in r1.recognize_google(audio):
            with mic as source:
                audio=r1.listen(source,timeout=5)
                try:
                    get = r1.recognize_google(audio)
                    
                    engine.say("Please Enter the Book Name ")
                    engine.runAndWait()
                    adding_book = input('Enter the Book you wish to Add')
                    
                    obj.add_book(adding_book)
                except:
                    print("Unable To Understand")
                    pass;
           
        elif 'rent book' in r2.recognize_google(audio):
            with mic as source:
                audio=r2.listen(source,timeout=5)
                try:
                    get = r2.recognize_google(audio)
                    
            
                    engine.say("Please Enter your name");
                    engine.runAndWait()
                    user_name = input('Enter your name : ')
                    
                    engine.say("Please Enter Book Name")
                    engine.runAndWait()
                    user_book = input('Enter the Book name You want to lend :(Case-Sensitive) ')
                    
                    book1='Python'
                    book2='Let us C'
                    book3='Javascript & Jquery'
                    book4='Machine Learning' 
                    book5='Head First JAVA'
                    book6='HTML & CSS'
                    book7='C++ By SUMITA ARORA'
                    book9='Engineering Mathematics'
                    book10='RD Sharma Class 10'
                    book11='RD Sharma Class 11'
                    book12='RD Sharma Class 12'
                    book13='Engineering Physics'
                    book14='Aeronautical Studies'
                    book15='Together Chemistry'
                    book16='Together Mathematics'
                    book17='Encyclopedia'
                    book18='RS Aggarwal'
                    book19='Begin with C#'
                    book20='SL Arora'
                    book8=adding_book
                    if user_book == book1 :
                        obj.lend_book(user_name, user_book)
                    
                    elif user_book==book2:
                        obj.lend_book(user_name, user_book)
                    
                    elif user_book==book3:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book4:
                        obj.lend_book(user_name, user_book)
                    
                    elif user_book==book5:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book6:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book ==book7:
                        obj.lend_book(user_name, user_book)
                    
                    elif user_book==book8:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book9:
                        obj.lend_book(user_name, user_book)  
                        
                    elif user_book==book10:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book11:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book12:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book13:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book14:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book15:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book16:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book17:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book18:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book19:
                        obj.lend_book(user_name, user_book)
                        
                    elif user_book==book20:
                        obj.lend_book(user_name, user_book)  
                        
                    else:
                        print("\nSORRY ! BOOK IS NOT AVAIABLE RIGHT NOW ");
                        engine.say("SORRY ! BOOK IS NOT AVAIABLE RIGHT NOW")
                        engine.runAndWait()
                        print("\nNOTE : YOUR BOOK WILL BE MADE AVAILABLE WITHIN A WEEK")
                        engine.say("YOUR BOOK WILL BE MADE AVAILABLE WITHIN A WEEK")
                        engine.runAndWait()
                except:
                      print("Unable To Undersatnd")
                      pass;
                   
                
           

        elif 'return book' in r4.recognize_google(audio):
            with mic as source:
                audio=r4.listen(source,timeout=5)
                try:
                     engine.say("Please Enter The Book name That You Want To Return")
                     engine.runAndWait()
                     returning_book = input('Enter The Book name That You Want To Return(Case-Sensitive) : ')
                     obj.return_book(returning_book)
                except:
                    print("Unable to understand")
       
        
        elif 'exit' in r3.recognize_google(audio):
            with mic as source:
                audio=r3.listen(source,timeout=5)
                try:
                    get = r3.recognize_google(audio)
                    
                    
                    engine.say("THANKS ! PLEASE VISIT AGAIN");
                    engine.runAndWait()
                    sys.exit()
                except:
                     
                     sys.exit()
                     
     
     
       
            
            
        engine.say("WANT TO DO SOMETHING ELSE ALSO ?")
        engine.runAndWait()    
        user_input = int(
        input('WANT TO DO SOMETHING ELSE ALSO ?\n1. Continue.\n2. Exit.\n'))
            
        
        if user_input is 1:
            engine.say("SURE ");
            engine.runAndWait()
    
            continue
    
        else:
                
             print("THANK YOU ! PLEASE VISIT AGAIN")
        engine.say("THANK YOU ! PLEASE VISIT AGAIN")
        engine.runAndWait()
    
        
        sys.exit()

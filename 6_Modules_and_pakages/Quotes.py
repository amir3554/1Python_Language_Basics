quotes_list = ["For every complex probles there is an answer that is clear , simple , and wrong.",
          "You can't be successful in business with out taking a risk. its really that simple.",
          "Only great minds can afford a simple style."]

def get_quotes():
    return print("\n".join(quotes_list))

def add_quotes(quote):
    if isinstance(quote, str):#تأخذ هذه الدالة وسيطين الاول هو الكائن الذي نرغب ب التحقق منه و الثاني هو نوع الصنف و تعيد قيمة صحيحة او خاطئة حسب التشابه
        quotes_list.append(quote)
    else:
        print("The quote must be a string.")

def get_random_qoute():
    from random import choice
    return choice(quotes_list)

#another qoute : You only live once , but if you do it right , once is enough


if __name__ == "__main__":#This code runs only if the file is executed directly.
    get_random_qoute()
    add_quotes("another qoute : You only live once , but if you do it right , once is enough")
    get_quotes()



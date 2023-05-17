# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library

from tkinter import Tk, Label,Button,Text,END,Frame

def get_alphabet(s):
    o=""
    for c in s:
        if c.isalpha():
            o += c
    return o

def select():
    text_out.delete("1.0",END)
    s = text_sequence.get("1.0",END)
    
    s = get_alphabet(s)

    r = text_query.get("1.0",END)
    r = r.strip()
    r = r.split(',')
    new_s = ''
    for item in r:
        r1 = item.split('-')
        if len(r1) == 2:
            for i in range(int(r1[0]),int(r1[1])+1):
                if i<len(s):
                    new_s+=s[i-1]
        else:
            if int(r1[0])<len(s):
                new_s+=s[int(r1[0])-1]
    text_out.insert("1.0", new_s)

def search():
    s = text_sequence.get("1.0",END)
    s = get_alphabet(s)

    q = text_query.get("1.0",END)
    q = get_alphabet(q)    
    if len(q) < 1:
        return 0
    
    indices = []
    for i in range(len(s)-len(q)):
        print(s[i:i + len(q)])
        print(q)
        if s[i:i + len(q)] == q:
            indices.append(i)
    print(indices)
    new_s = ""
    for i,c in enumerate(s):
        if i - len(q) in indices:
            new_s += "] "
        if i in indices:
            new_s += " ["

        new_s += c
        
    text_out.delete("1.0",END)
    text_out.insert("1.0", new_s)


def format():
    s = text_sequence.get("1.0",END)
    s = get_alphabet(s)

    r = text_query.get("1.0",END)
    r = r.strip()
    try:
        r = int(r)
    except:
        r = 60

    text_query.delete("1.0",END)
    text_query.insert("1.0", str(r))

    new_s = ""
    for i, item in enumerate(s):
        if i%r == 0:
            if i == 0:
                new_s += "{0:8d}".format(i+1)
            else:
                new_s += "\n{0:8d}".format(i+1)

        if i%10 == 0:
            new_s += " "
        
        new_s += item

    text_out.delete("1.0",END)
    text_out.insert("1.0", new_s)

def unformat():
    s = text_sequence.get("1.0",END)
    s = get_alphabet(s)

    text_out.delete("1.0",END)
    text_out.insert("1.0", s)

def reverse():
    s = text_sequence.get("1.0",END)
    s = get_alphabet(s)

    text_out.delete("1.0",END)
    text_out.insert("1.0", s[::-1])

def antisense_DNA():
    s = text_sequence.get("1.0",END)
    s = get_alphabet(s)
    new_s = ""
    for i,c in enumerate(s):
        d=c
        if c == 'A':
            d = 'T'
        if c == 'T':
            d = 'A'
        if c == 'C':
            d = 'G'
        if c == 'G':
            d = 'C'
        if c == 'a':
            d = 't'
        if c == 't':
            d = 'a'
        if c == 'c':
            d = 'g'
        if c == 'g':
            d = 'c'
        new_s += d

    text_out.delete("1.0",END)
    text_out.insert("1.0", new_s)

def antisense_RNA():
    s = text_sequence.get("1.0",END)
    s = get_alphabet(s)
    new_s = ""
    for i,c in enumerate(s):
        d = c
        if c == 'A':
            d = 'U'
        if c == 'U':
            d = 'A'
        if c == 'C':
            d = 'G'
        if c == 'G':
            d = 'C'
        if c == 'a':
            d = 'u'
        if c == 'u':
            d = 'a'
        if c == 'g':
            d = 'c'
        if c == 'c':
            d = 'g'
        new_s += d

    text_out.delete("1.0",END)
    text_out.insert("1.0", new_s)
	
def upper_case():
    s = text_sequence.get("1.0",END)
    s = get_alphabet(s)
    text_out.delete("1.0",END)
    text_out.insert("1.0", s.upper())

def lower_case():
    s = text_sequence.get("1.0",END)
    s = get_alphabet(s)
    text_out.delete("1.0",END)
    text_out.insert("1.0", s.lower())


if __name__ == '__main__':																								
    # Create the root window
    window = Tk()
    window.title('sequence tool')
    window.geometry("850x780")
    #window.config(background = "gray")

    left_frame = Frame(window, width=50, height=750)
    left_frame.grid(row=0, column=0, padx=[20,0], pady=10)
    right_frame = Frame(window, width=700, height=750)
    right_frame.grid(row=0, column=1, padx=[0,20], pady=10)
        
    label_sequence = Label(right_frame, text="sequence",
                                width=100, height=1, fg="blue")
    label_sequence.grid(column = 1, row = 1)

    text_sequence = Text(right_frame, height = 20, width = 80)
    text_sequence.grid(column = 1, row = 2)

    label_range = Label(right_frame,text = "query", width=70, height=1, fg="blue")
    label_range.grid(column = 1, row = 3)

    text_query = Text(right_frame, height = 1, width = 80)
    text_query.grid(column = 1, row = 4)

    label_out = Label(right_frame, text = "out", width = 100, height = 1, fg = "blue")
    label_out.grid(column = 1, row = 5)
    text_out = Text(right_frame, height = 20, width = 80)
    text_out.grid(column = 1, row = 6)

    blank = Label(right_frame, text = "", width = 100, height = 1, fg = "blue")
    blank.grid(column = 1, row = 7)




    button_select = Button(left_frame,
                        text = "select", width = 12,
                        command = select)
    button_select.grid(column = 1,row = 1)

    button_search = Button(left_frame,
                        text = "search", width = 12,
                        command = search)
    button_search.grid(column = 1,row = 2)

    spacer1 = Label(left_frame, text="")
    spacer1.grid(column=1, row=3)

    button_format = Button(left_frame,
                    text = "format",width = 12,
                    command = format)
    button_format.grid(column = 1,row = 4)

    button_format = Button(left_frame,
                    text = "unformat",width = 12,
                    command = unformat)
    button_format.grid(column = 1,row = 5)

    spacer2 = Label(left_frame, text="")
    spacer2.grid(column=1, row=6)

    button_format = Button(left_frame,
                    text = "reverse",width = 12,
                    command = reverse)
    button_format.grid(column = 1,row = 7)

    button_format = Button(left_frame,
                    text = "antisense_DNA",width = 12,
                    command = antisense_DNA)
    button_format.grid(column = 1,row = 8)

    button_format = Button(left_frame,
                    text = "antisense_RNA",width = 12,
                    command = antisense_RNA)
    button_format.grid(column = 1,row = 9)

    spacer3 = Label(left_frame, text="")
    spacer3.grid(column=1, row=10)

    button_format = Button(left_frame,
                    text = "upper_case",width = 12,
                    command = upper_case)
    button_format.grid(column = 1,row = 11)

    button_format = Button(left_frame,
                    text = "lower_case",width = 12,
                    command = lower_case)
    button_format.grid(column = 1,row = 12)

    spacer3 = Label(left_frame, text="")
    spacer3.grid(column=1, row=13)

    window.mainloop()

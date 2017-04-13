import unittest

class Item(): 

    def __init__(self, item_id, title, author, location): 
        self.item_id = item_id
        self.title = title
        self.author = author
        self.location = location

    def report(self): 
        return  'Title: {}\nItem ID: {}\nAuthor: {}\nLocation: {}'.format(self.title, self.item_id, self.author, self.location)

class Book(Item): 

    def __init__(self, item_id, title, author, location, pages): 
        super().__init__(item_id, title, author, location)
        self.pages = pages

    def report(self): 
        output = super().report()
        return output + '\nPAGES: {}'.format(self.pages)

    def book_length(self): 
        if self.pages <0: 
            return 'This book has an invalid number of pages'
        elif float(self.pages).is_integer(): 
            return 'This book has an invalid number of pages'
        elif self.pages < 10: 
            return 'This is basically a pamphlet.'
        elif self.pages < 501: 
            return "Yeah, this is a book, congrats."
        elif self.pages > 500: 
            return 'We\'ve got a reader here!'
        else: 
            return 'This book has an invalid number of pages'

class Audio(Item): 
    def __init__(self, item_id, title, author, location, audio_format): 
        super().__init__(item_id, title, author, location)
        self.audio_format = audio_format

    def report(self): 
        output = super().report()
        return output + '\nFORMAT: '.format(self.audio_format)

    def player(self): 
        try: 
            if self.audio_format.lower()  == 'cd': 
                player = 'Discman'
            elif self.audio_format.lower() == 'vhs': 
                player = 'VCR'
            elif self.audio_format.lower() == 'mp3':
                player = 'iPod or computer'
            else: 
                player = 'UNKNOWN'
            return 'The player you need for this media is: {}'.format(player)
        except: 
            return 'The audio format is invalid'

class BookTestCase(unittest.TestCase):
    def test_book_length(self):
        page_num = [0, 1, -1, 1000, 250, 5, 0.5]
        for i in page_num: 
            book = Book(123, 'Title', 'Author', 'Location', i)
            result = book.book_length()
            self.assertEqual(type(result), str)

class AudioTestCase(unittest.TestCase): 
    def test_unknown_audio_format(self): 
        audio = Audio(123, 'Title', 'Author', 'Location', 'mango')
        result = audio.player()
        self.assertEqual(result, 'The player you need for this media is: UNKNOWN')
    def test_comprehensive_audio_formats(self): 
        audio_formats = ['cd', 'VHS', 'mp3']
        for i in audio_formats: 
            audio = Audio(123, 'Title', 'Author', 'Location', i)
            result = audio.player()
            self.assertFalse('UNKNOWN' in result)

if __name__ == "__main__":
    unittest.main()
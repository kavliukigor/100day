from scraper import Scraper
from form_filler import Filler

scraper = Scraper()
filler=Filler()
links, prices, adresses=scraper.get_bookings()
filler.fill(links, prices, adresses)
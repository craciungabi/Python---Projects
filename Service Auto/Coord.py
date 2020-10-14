from Repository.RepositoryGeneric import Repository
from Service.ServiceMasina import ServiceMasina
from Service.ServiceCard import ServiceCard
from Service.ServiceTranzactie import ServiceTranzactie
from UI.Console import Console

car_repository = Repository('cars.pkl')
card_repository = Repository('card.pkl')
tranzactie_repository = Repository('tranzactie.pkl')

car_service = ServiceMasina(car_repository)
card_client_service = ServiceCard(card_repository)
tranzactie_service = ServiceTranzactie(tranzactie_repository, card_repository, car_repository)

console = Console(car_service, card_client_service, tranzactie_service)

console.run_console()



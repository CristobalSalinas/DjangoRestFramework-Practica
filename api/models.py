from django.db import models

class Provider(models.Model):
    id_provider = models.AutoField(primary_key=True)
    name_provider = models.CharField(max_length=255)
    detail_provider = models.CharField(max_length=255)

    def __str__(self):
        return self.name_provider


class Etf(models.Model):
    id_etf = models.TextField(primary_key=True) 
    ticker_etf = models.TextField(blank=True, null=True)  
    description_etf = models.TextField(blank=True, null=True) 
    assetclass_etf = models.TextField(blank=True, null=True) 
    aum_etf = models.TextField(blank=True, null=True) 
    category_etf = models.TextField(blank=True, null=True)  
    inceptiondate_etf = models.DateTimeField(blank=True, null=True) 
    brand_etf = models.TextField(blank=True, null=True) 
    legalstructure_etf = models.TextField(blank=True, null=True)  
    indextracked_etf = models.TextField(blank=True, null=True) 
    issuer_etf = models.TextField(blank=True, null=True) 
    markettype_etf = models.TextField(blank=True, null=True)
    focus_etf = models.TextField(blank=True, null=True) 
    fund_etf = models.TextField(blank=True, null=True) 
    geography_etf = models.TextField(blank=True, null=True)  
    niche_etf = models.TextField(blank=True, null=True)  
    region_etf = models.TextField(blank=True, null=True)  
    visibility_etf = models.BooleanField(default=False)
    provider_id = models.ForeignKey(Provider,on_delete=models.CASCADE)

    def __str__(self):
        return self.ticker_etf

class Component(models.Model):
    id_comp = models.AutoField(primary_key=True)
    name_comp = models.CharField(max_length=255)
    identifier_comp = models.CharField(max_length=255)
    weigth_comp = models.FloatField()
    sector_comp = models.CharField(max_length=255)
    shares_comp = models.FloatField()
    etf_id = models.ForeignKey(Etf,on_delete=models.CASCADE)

    def __str__(self):
        return self.name_comp


class Price(models.Model):
    id_price = models.AutoField(primary_key=True)
    price_price = models.FloatField()
    nav_price = models.FloatField()
    bid_ask_price = models.FloatField()
    premiun_price = models.FloatField()
    ytd_price = models.FloatField()
    expanses_price = models.FloatField()
    earnings_price = models.FloatField()
    book_price = models.FloatField()
    date_price = models.DateTimeField(auto_now=False)
    etf_price = models.ForeignKey(Etf,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_price)


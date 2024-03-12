offene_MPS = """SELECT  BELEGNR as 'PO', 
		ARTIKELNR as 'ArticleNr', 
		BEZEICHNUNG as 'ArticleDescription', 
		LIEFERDATUM as 'Delivery Date',
	    DATEDIFF(day, GETDATE(),[LIEFERDATUM]) 'Days before Delivery Date',
		LIEFERANTENNR

  FROM [emea_enventa_live].[dbo].[BESTELLPOS]
  where BELEGART in (2,191) --nur PM bzw. AsienFW
  and status = 1 -- nur offene Bestellungen
  and DATEDIFF(day, GETDATE(),[LIEFERDATUM]) < 14 --erinnerung X Tage vor Lieferdatum
  and PE14_SampleReceived is null


  order by LIEFERDATUM"""


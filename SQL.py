offene_MPS = """SELECT  BELEGNR as 'PO', 
		ARTIKELNR as 'ArticleNr', 
		BEZEICHNUNG as 'ArticleDescription', 
		LIEFERDATUM as 'Delivery Date',
	    DATEDIFF(day, GETDATE(),[LIEFERDATUM]) 'Days before Delivery Date',
		PE14_SampleReceived as 'MPS Received'

  FROM [emea_enventa_live].[dbo].[BESTELLPOS]
  where LIEFERANTENNR = 70053 --definiere welche Lieferanten
  and status = 1 -- nur offene Bestellungen
  and DATEDIFF(day, GETDATE(),[LIEFERDATUM]) < 1 --erinnerung X Tage vor Lieferdatum
  and PE14_SampleReceived is null


  order by LIEFERDATUM"""


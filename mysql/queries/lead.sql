USE lead_gen_business;

###########################################################################
#	1. What query would you run to get the total revenue for March of 2012?

SELECT MONTHNAME(billing.charged_datetime) AS month, sum(amount) AS revenue FROM billing
WHERE billing.charged_datetime <= "2012/03/31" AND billing.charged_datetime >= "2012/03/01" 
;

###########################################################################

#	2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT billing.client_id, sum(amount) AS total_revenue FROM billing
WHERE client_id=2
;

###########################################################################
#	3. What query would you run to get all the sites that client=10 owns?

SELECT sites.domain_name AS website, clients.client_id FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
WHERE clients.client_id = 10;

#################################################################################
#	4a. What query would you run to get total # of sites created per month per
#	year for the client with an id of 1?

SELECT clients.client_id, count(sites.site_id) AS number_of_websites, MONTHNAME(sites.created_datetime) AS month_created, YEAR(sites.created_datetime) AS Year FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
WHERE clients.client_id = 1
GROUP BY  month_created, Year
;

#################################################################################
#	4b. What query would you run to get total # of sites created 
#	per month per year for the client with an id of 20?

SELECT clients.client_id, count(sites.site_id) AS number_of_websites, MONTHNAME(sites.created_datetime) AS month_created, YEAR(sites.created_datetime) AS Year FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
WHERE clients.client_id = 20
GROUP BY  month_created, Year
;

#####################################################################################
#	5. What query would you run to get the total # of leads generated 
#	for each of the sites between January 1, 2011 to February 15, 2011?
SELECT sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads FROM sites
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime >= "2011/01/01" AND leads.registered_datetime <= "2011/02/15"
GROUP BY sites.domain_name
;

#####################################################################################
#	6. What query would you run to get a list of client names and the total # of leads 
#	we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT CONCAT(clients.first_name, " " , clients.last_name) AS client, COUNT(leads.leads_id) AS number_of_leads FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime >= "2011/01/01" AND leads.registered_datetime <= "2011/12/31"
GROUP BY client
;

#####################################################################################
#	7. What query would you run to get a list of client names and the total # of leads
#	we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT CONCAT(clients.first_name, " " , clients.last_name) AS client, COUNT(leads.leads_id) AS number_of_leads, MONTHNAME(leads.registered_datetime) AS month_generated FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime >= "2011/01/01" AND leads.registered_datetime <= "2011/06/30"
GROUP BY client, month_generated
;

#####################################################################################
#	8a. What query would you run to get a list of client names and the total # of leads 
#	we've generated for each of our clients between January 1, 2011 to December 31, 2011?
#	 Order this query by client id.

SELECT CONCAT(clients.first_name, " " , clients.last_name) AS client,sites.domain_name AS website, COUNT(leads.leads_id)  AS number_of_leads FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime >= "2011/01/01" AND leads.registered_datetime <= "2011/12/31"
GROUP BY client, website
ORDER BY clients.client_id
;

#####################################################################################
#	8b.Come up with a second query that shows all the clients, the site name(s),
#	and the total number of leads generated from each site for all time.

SELECT CONCAT(clients.first_name, " " , clients.last_name) AS client,sites.domain_name AS website, COUNT(leads.leads_id)  AS number_of_leads FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
GROUP BY client, website
;

#####################################################################################
#	9a. Write a single query that retrieves total revenue collected from each
#	client for each month of the year. Order it by client id. With month id
SELECT CONCAT(clients.first_name, " " , clients.last_name) AS client_name, sum(billing.amount) AS total_revenue, MONTH(billing.charged_datetime) AS month_charged, YEAR(billing.charged_datetime) AS year_charged FROM clients
LEFT JOIN billing ON clients.client_id = billing.client_id
GROUP BY CONCAT(clients.first_name, " " , clients.last_name), month_charged, year_charged
ORDER BY clients.client_id, year_charged, month_charged
;


#####################################################################################
#	9b. Write a single query that retrieves total revenue collected from each
#	client for each month of the year. Order it by client id. With month id
#	 With month name.
SELECT CONCAT(clients.first_name, " " , clients.last_name) AS client_name, sum(billing.amount) AS total_revenue, MONTH(billing.charged_datetime) AS month_charged, YEAR(billing.charged_datetime) AS year_charged FROM clients
LEFT JOIN billing ON clients.client_id = billing.client_id
GROUP BY clients.client_id, month_charged, year_charged
ORDER BY clients.client_id, year_charged, month_charged
;

#####################################################################################
#	10. Write a single query that retrieves all the sites that each client owns.
#	Group the results so that each row shows a new client. 
#	It will become clearer when you add a new field called 'sites' 
#	that has all the sites that the client owns. 
#	(HINT: use GROUP_CONCAT)

SELECT CONCAT(clients.first_name, " " , clients.last_name) AS client_name, GROUP_CONCAT(sites.domain_name) AS sites FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
GROUP BY  clients.client_id
;

 
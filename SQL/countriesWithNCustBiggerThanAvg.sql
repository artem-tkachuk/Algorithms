/* Return all countries with the # of cusomers > average # of customers of all cities  */

SELECT city.city_name, country.country_name, COUNT(customer.id) AS num_customer
    FROM city
        JOIN country ON city.country_id = country.id
        JOIN customer ON city.id = customer.city_id

            GROUP BY city.id

                HAVING num_customer > (
                    SELECT AVG(num_customer) 
                        FROM (
                            SELECT city.id, COUNT(customer.id) AS num_customer
                                FROM city
                                    JOIN country ON city.country_id = country.id
                                    JOIN customer ON city.id = customer.city_id
                                        GROUP BY city.id
                        ) AS placeholder
                )

                    ORDER BY country.country_name;









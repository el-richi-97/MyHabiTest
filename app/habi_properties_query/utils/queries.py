class QueryMaker:

    @staticmethod
    def get_query(filters: dict) -> tuple[str, tuple]:
        """
        This method is used to get a final query string and values for use with the connection library and get the
        results for the properties_query microservice. Is recommended to provide a dictionary for this method to get a
        proper filtered query but it's not mandatody. Instead, please give an empty dictionary if you don't want to
        provide more filters than the default filter of status names. This method is dynamic and could be used with
        the wanted filters.

        :param filters: dictionary when the user can set the wanted values and keys for the WHERE clause of the query.
        :return: tuple (query_string, value_tuple) where query_string is the final query for use with the connection
        and value_tuple is the tuple of values to use in the execute method and replace the placeholders in the query.
        """

        if filters:
            filters['name'] = filters.pop('status', None)

        final_filters = [f'{key} = %s' for key, value in filters.items() if value is not None]

        result = 'WHERE ' + ' AND '.join(final_filters + ["st.name IN (%s, %s, %s) AND price > 0"])

        query = f"""
            SELECT pr.address, pr.city, st.name AS status, pr.price as sale_price, pr.description
            FROM (
                SELECT property_id, MAX(update_date) AS last_update_date
                FROM status_history
                GROUP BY property_id
            ) AS sh_last
            JOIN status_history sh ON sh_last.property_id = sh.property_id AND sh_last.last_update_date = sh.update_date
            JOIN status st ON sh.status_id = st.id
            JOIN property pr ON sh.property_id = pr.id
            {result};
        """

        values = tuple(list(filters.values()) + ['pre_venta', 'en_venta', 'vendido'])

        return query, values


if __name__ == '__main__':
    query_maker = QueryMaker()

    test_filters = {
        "year": 2021,
        "city": "bogota",
        "status": "en_venta"
    }

    test_query, test_values = query_maker.get_query(test_filters)
    print(f'Query result: {test_query}')
    print(f'Values result: {test_values}')

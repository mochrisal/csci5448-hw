import random

class Tool(object):
    def __init__(self, name, price_per_night):
        self.name = name
        self.price_per_night = price_per_night

    def __repr__(self):
        return "{}".format(self.name, self.price_per_night)


class PaintingTool(Tool):
    def __init__(self, name):
        Tool.__init__(self, name, 3.00)


class ConcreteTool(Tool):
    def __init__(self, name):
        Tool.__init__(self, name, 9.50)


class PlumbingTool(Tool):
    def __init__(self, name):
        Tool.__init__(self, name, 7.25)


class WoodworkTool(Tool):
    def __init__(self, name):
        Tool.__init__(self, name, 11.75)


class YardworkTool(Tool):
    def __init__(self, name):
        Tool.__init__(self, name, 4.50)


class Rental(object):
    def __init__(self, day_rented, nights_rented, tools):
        self.day_rented = day_rented
        self.nights_rented = nights_rented
        self.nights_remaining = nights_rented
        self.tools = tools

        self.day_returned = None

        self.price = sum(self.tools[tool_id].price_per_night for tool_id in self.tools) * self.nights_rented

    def __repr__(self):
        return "Tools = {}, Days = {}-{}".format(list(self.tools[tool_id].name for tool_id in self.tools), 
                                                 self.day_rented, self.day_rented+self.nights_rented)

    def daily_update(self, current_day):
        self.nights_remaining = self.nights_remaining - 1
        if(self.nights_remaining) == 0:
            self.day_returned = current_day

    def get_price(self):
        return self.price

    def get_tools(self):
        return self.tools


class Customer(object):
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def __repr__(self):
        return "{} ({} rentals, {} tools)".format(self.name, len(self.get_rentals()), len(self.get_tools_rented().keys()))

    def rent(self, day, nights, tools):
        rental = Rental(day, nights, tools)
        self.rentals.append(rental)
        return rental

    def return_rentals(self):
        returned_rentals = []
        for rental in self.rentals:
            if rental.nights_remaining == 0:
                returned_rentals.append(rental)
                self.rentals.remove(rental)
        return returned_rentals

    def update_rentals(self, day):
        for rental in  self.rentals:
            rental.daily_update(day)
        return self.return_rentals()

    def get_rentals(self):
        return self.rentals

    def get_tools_rented(self):
        tools = {}

        for rental in self.rentals:
            tools.update(rental.get_tools())

        return tools

    def get_num_tools_rented(self):
        return len(self.get_tools_rented())

class CasualCustomer(Customer):
    def __init__(self, name):
        self.min_tools = 1
        self.max_tools = 2
        self.min_nights = 1
        self.max_nights = 2

        Customer.__init__(self, name)

class RegularCustomer(Customer):
    def __init__(self, name):
        self.min_tools = 1
        self.max_tools = 3
        self.min_nights = 3
        self.max_nights = 5

        Customer.__init__(self, name)

class BusinessCustomer(Customer):
    def __init__(self, name):
        self.min_tools = 3
        self.max_tools = 3
        self.min_nights = 7
        self.max_nights = 7

        Customer.__init__(self, name)

class Store(object):
    def __init__(self, customers, catalog):
        self.customers = customers
        self.catalog = catalog
        self.inventory = catalog
        self.payments = 0
        self.day = 0

    def rent(self, customer, day, nights, tools):
        rental = customer.rent(day, nights, tools)
        for tool_id in tools.keys():
            del self.inventory[tool_id]
        self.payments += rental.get_price()
        return rental

    def update_rentals(self, day):
        returned_rentals = []

        for customer_id in self.customers:
            returned_rentals += self.customers[customer_id].update_rentals(day)

        for rental in returned_rentals:
            for tool_id in rental.tools.keys():
                self.inventory[tool_id] = rental.tools[tool_id]

        return returned_rentals

    def get_inventory(self):
        return self.inventory

    def get_num_available_tools(self):
        return len(self.get_inventory())

    def get_rentals(self):
        rentals = []
        for customer_id in self.customers:
            for rental in self.customers[customer_id].rentals:
                rentals.append(rental)
        return rentals

    def get_rented_tools(self):
        tools = {}

        for rental in self.get_rentals():
            for tool_id in rental.tools:
                tools[tool_id] = rental.tools[tool_id]

        return tools

    def get_num_rented_tools(self):
        return len(self.get_rented_tools())

    def get_total_payments(self):
        return self.payments

class Simulation(object):
    def __init__(self):
        self.customers = {
            1: CasualCustomer('Casual Customer 1'),
            2: CasualCustomer('Casual Customer 2'),
            3: CasualCustomer('Casual Customer 3'),
            4: CasualCustomer('Casual Customer 4'),

            5: RegularCustomer('Regular Customer 1'),
            6: RegularCustomer('Regular Customer 2'),
            7: RegularCustomer('Regular Customer 3'),

            8: BusinessCustomer('Business Customer 1'),
            9: BusinessCustomer('Business Customer 2'),
            10: BusinessCustomer('Business Customer 3')
        }

        self.catalog = {
            1: PaintingTool('Painting Tool 1'),
            2: PaintingTool('Painting Tool 2'),
            3: PaintingTool('Painting Tool 3'),
            4: PaintingTool('Painting Tool 4'),

            5: ConcreteTool('Concrete Tool 1'),
            6: ConcreteTool('Concrete Tool 2'),
            7: ConcreteTool('Concrete Tool 3'),
            8: ConcreteTool('Concrete Tool 4'),

            9: PlumbingTool('Plumbing Tool 1'),
            10: PlumbingTool('Plumbing Tool 2'),
            11: PlumbingTool('Plumbing Tool 3'),
            12: PlumbingTool('Plumbing Tool 4'),

            13: WoodworkTool('Woodwork Tool 1'),
            14: WoodworkTool('Woodwork Tool 2'),
            15: WoodworkTool('Woodwork Tool 3'),
            16: WoodworkTool('Woodwork Tool 4'),

            17: YardworkTool('Yardwork Tool 1'),
            18: YardworkTool('Yardwork Tool 2'),
            19: YardworkTool('Yardwork Tool 3'),
            20: YardworkTool('Yardwork Tool 4')
        }

        self.store = Store(self.customers, self.catalog)

    def simulate_customer_rental(self, day, customer_id):
        print("\t{}".format(self.store.customers[customer_id]))
        print("\t{} arrives in store.".format(self.store.customers[customer_id].name))

        if self.store.customers[customer_id].get_num_tools_rented() >= self.store.customers[customer_id].max_tools:
            print("\t{} already has maximum tools rented ({}), and so leaves the store without renting.".format(
                                                                                 self.store.customers[customer_id].name, 
                                                                           self.store.customers[customer_id].max_tools))

        elif self.store.customers[customer_id].min_tools > self.store.get_num_available_tools():
            print("\t{} wants at least {} tools ({} available), and so leaves store without renting.".format(
                                                                            self.store.customers[customer_id].name,
                                                                            self.store.customers[customer_id].max_tools,
                                                                            self.store.get_num_available_tools()))
        else:
            # Choose a random number of nights within range.
            nights = random.randint(self.store.customers[customer_id].min_nights, 
                                    self.store.customers[customer_id].max_nights)

            # Choose a list of random tools from the available inventory
            num_tools = random.randint(self.store.customers[customer_id].min_tools, 
                            min(self.store.customers[customer_id].max_tools, self.store.get_num_available_tools()))

            # print(self.store.customers[customer_id].min_tools)
            # print(self.store.get_num_available_tools())
            # print(self.store.get_inventory().keys())
            # print(num_tools)
            tool_id_list = random.sample(self.store.get_inventory().keys(), num_tools)

            # Add the randomized available tools to a dict
            tools = {}
            for tool_id in tool_id_list:
                tools[tool_id] = self.store.inventory[tool_id]

            # Have the customer rent the randomized tools for the randomized number of nights.
            rental = self.store.rent(self.store.customers[customer_id], day, nights, tools)
            print("\t{} pays ${:.2f} to rent {} tools for {} nights".format(self.store.customers[customer_id], 
                                                                               rental.get_price(), num_tools, nights))
            print("\t\t{}".format(rental))
            print("\t{}".format(self.store.customers[customer_id]))
        print("\n")

    def simulate_returns(self, day):
        # Update all rentals for new day.
        returned_rentals = self.store.update_rentals(day)
        if not returned_rentals:
            print("No returns today.")
        else:
            for rental in returned_rentals:
                print("\t{}".format(rental))

    def simulate_day(self, day):
        print("DAY {}".format(day))

        print("Returns")
        self.simulate_returns(day)
        print("\n")

        print("Available Tools: {}".format(self.store.get_num_available_tools()))
        print("Rented Tools: {}".format(self.store.get_num_rented_tools()))
        print("Total Payments: ${}\n".format(self.store.get_total_payments()))
        print("\n")

        # Choose 1-5 random customers to arrive today
        customers_today = random.sample(range(1,11), random.randint(1,6))

        print("Rentals")
        # Each customer will see if they can make a rental
        for customer_id in customers_today:
            self.simulate_customer_rental(day, customer_id)

    def run_simulation(self, days):
        print("Running Simlulation..\n")
        print("Customers:")
        for customer_id in self.store.customers:
            print("\t{}".format(self.store.customers[customer_id].name))
        print("\n")

        print("Tool Catalogue:")
        for tool_id in self.store.catalog:
            print("\t{}".format(self.store.catalog[tool_id].name))
        print("\n")

        for day in range(1,days+1):
            self.simulate_day(day)


sim = Simulation()
sim.run_simulation(36)
from spring import Spring


class SpringArray:

    def equivalent_spring(self, spring_expression, springs=None):
        spring = Spring(k=0)
        for current in springs:
            spring = spring.in_parallel(current)

        print(spring)
        return spring

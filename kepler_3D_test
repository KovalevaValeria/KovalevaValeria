        self.universe = universe
        self.mass = mass
        self.position = position
        self.velocity = velocity
        universe.add_body(self)

        self.ptrace = [self.position.copy()]
        self.vtrace = [self.velocity.copy()]

    def force_induced_by_other(self, other):
        """Сила, с которой другое тело действует на данное"""
        delta_p = other.position - self.position
        distance = numpy.linalg.norm(delta_p)  # Евклидова норма (по теореме Пифагора)
        force_direction = delta_p / distance
        force = force_direction * self.mass * other.mass * \
                self.universe.gravity_flow_dencity_per_1_1(distance)
        return force

    def advance(self):
        """Перемещаем тело, исходя из его скорости"""
        self.position += self.velocity * MODEL_DELTA_T
        self.ptrace.append(self.position.copy())
        self.vtrace.append(self.velocity.copy())

    def apply_force(self, force):
        """Изменяем скорость, исходя из силы, действующей на тело"""
        self.velocity += force * MODEL_DELTA_T / self.mass


class Universe2D(Universe):
    def __init__(self,
                 G,  # гравитационная постоянная
                 k,  # коэффициент при упругом соударении
                 collision_distance  # всё-таки это не точки
                 ):
        super().__init__()
        self.G = G
        self.k = k
        self.collision_distance = collision_distance

    def gravity_flow_dencity_per_1_1(self, dist):

        if dist > self.collision_distance:
            return self.G / dist
        else:
            return -self.k / dist


u = Universe2D(MODEL_G, COLLISION_COEFFICIENT, COLLISION_DISTANCE)


bodies = [
    MaterialPoint(u, 500., vec([0., 0.]), vec([0., 0.])),
    MaterialPoint(u, 10., vec([300., 0.]), vec([0., -10.])),
    MaterialPoint(u, 10., vec([0., 300.]), vec([15., 0.]))
]

steps = int(TIME_TO_MODEL / MODEL_DELTA_T)
for stepn in range(steps):
    u.model_step()

plt.gca().set_aspect('equal')

for b in bodies:
    plt.plot(*tuple(map(list, zip(*b.ptrace))))

plt.show()

def plt_kepler(same_fig=False):
    for b in bodies:
        ds = np.cross(b.ptrace, b.vtrace)

        x = range(0, len(ds))
        plt.plot(x, ds)

        if not same_fig:
            plt.show()
    if same_fig:
        plt.show()

plt_kepler()

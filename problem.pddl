(define
	(problem room)
	(:domain room)
	(:objects
		m1 - mug
		p1 - person
		r1 - room
	)
	(:init (has-mug p1 m1) (in-room p1 r1))
	(:goal (and (has-mug p1 m1) (in-room p1 r1)))
)

(define
	(domain room)
	(:requirements :strips :typing)
	(:types
		mug
		person
		room
	)
	(:predicates
		(cost )
		(has-mug ?p - person ?m - mug)
		(in-room ?p - person ?r - room)
	)
	(:action enter-room
		:parameters (?p - person ?r - room)
		:precondition (not (in-room ?p ?r))
		:effect (in-room ?p ?r)
	)
	(:action get-mug
		:parameters (?m - mug ?p - person ?r - room)
		:precondition (and (not (has-mug ?p ?m)) (in-room ?p ?r))
		:effect (and (has-mug ?p ?m) (in-room ?p ?r) (cost ))
	)
	(:action leave-mug
		:parameters (?m - mug ?p - person ?r - room)
		:precondition (and (in-room ?p ?r) (has-mug ?p ?m))
		:effect (and (in-room ?p ?r) (not (has-mug ?p ?m)))
	)
)
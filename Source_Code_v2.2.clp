;-------------------------------------------------------------------------------------
; Available templates.
(deftemplate car
    (slot registration_number)
    (slot state)
)

(deftemplate space
    (slot name)
    (slot floor)
    (slot state)
)

(deftemplate platform
    (slot name)
    (slot space)
    (slot state)
)

(deftemplate rmcar
    (slot registration_number)
    (slot state)
)

;-------------------------------------------------------------------------------------
; Adjacency lists.
(deffacts east_neighbors
    (east S1 S2)
    (east S2 S3)
    (east S4 S5)
    (east S5 S6)
    (east S7 S8)
    (east S8 S9)
    (east S10 S11)
    (east S11 S12)
    (east S13 S14)
    (east S14 S15)
    (east S16 S17)
    (east S17 S18)
)

(deffacts north_neighbors
    (north S1 S4)
    (north S2 S5)
    (north S3 S6)
    (north S7 S10)
    (north S8 S11)
    (north S9 S12)
    (north S13 S16)
    (north S14 S17)
    (north S15 S18)
)

(deffacts up_neighbors
    (up S2 S8)
    (up S8 S14)
)

;-------------------------------------------------------------------------------------
; Creates cars.
(deffacts cars

)

;-------------------------------------------------------------------------------------
; Cars for removal.
(deffacts rmcars

)

;-------------------------------------------------------------------------------------
; Creates platforms.
(deffacts platforms
    (platform (name P1) (space S1) (state EMPTY))
    (platform (name P2) (space S3) (state EMPTY))
    (platform (name P3) (space S4) (state EMPTY))
    (platform (name P4) (space S5) (state EMPTY))
    (platform (name P5) (space S6) (state EMPTY))
    (platform (name P6) (space S8) (state EMPTY))
    (platform (name P7) (space S9) (state EMPTY))
    (platform (name P8) (space S10) (state EMPTY))
    (platform (name P9) (space S11) (state EMPTY))
    (platform (name P10) (space S14) (state EMPTY))
    (platform (name P11) (space S15) (state EMPTY))
    (platform (name P12) (space S16) (state EMPTY))
    (platform (name P13) (space S17) (state EMPTY))
    (platform (name P14) (space S18) (state EMPTY))
)

;-------------------------------------------------------------------------------------
; Creates spaces.
(deffacts spaces
    (space (name S1) (floor 1) (state YES_PLATFORM) )
    (space (name S2) (floor 1) (state NO_PLATFORM) )
    (space (name S3) (floor 1) (state YES_PLATFORM) )
    (space (name S4) (floor 1) (state YES_PLATFORM) )
    (space (name S5) (floor 1) (state YES_PLATFORM) )
    (space (name S6) (floor 1) (state YES_PLATFORM) )
    (space (name S7) (floor 2) (state NO_PLATFORM) )
    (space (name S8) (floor 2) (state YES_PLATFORM) )
    (space (name S9) (floor 2) (state YES_PLATFORM) )
    (space (name S10) (floor 2) (state YES_PLATFORM) )
    (space (name S11) (floor 2) (state YES_PLATFORM) )
    (space (name S12) (floor 2) (state NO_PLATFORM) )
    (space (name S13) (floor 3) (state NO_PLATFORM) )
    (space (name S14) (floor 3) (state YES_PLATFORM) )
    (space (name S15) (floor 3) (state YES_PLATFORM) )
    (space (name S16) (floor 3) (state YES_PLATFORM) )
    (space (name S17) (floor 3) (state YES_PLATFORM) )
    (space (name S18) (floor 3) (state YES_PLATFORM) )
)

;-------------------------------------------------------------------------------------
; Moves platform west.
(defrule move_west
    (declare (salience 10))
    ?x<-(space (name ?s) (floor ?temp) (state YES_PLATFORM))
        (east ?snew ?s)
    ?y<-(space (name ?snew) (floor ?temp1) (state NO_PLATFORM))
    ?z<-(platform (name ?pn) (space ?s) (state ?temp2))

    =>
        (modify ?x (state NO_PLATFORM))
        (modify ?y (state YES_PLATFORM))
        (modify ?z (space ?snew))
)

;-------------------------------------------------------------------------------------
; Moves platform east.
(defrule move_east
    (declare (salience 10))
    ?x<-(space (name ?s) (floor ?temp) (state YES_PLATFORM))
        (east ?s ?snew)
    ?y<-(space (name ?snew) (floor ?temp1) (state NO_PLATFORM))
    ?z<-(platform (name ?pn) (space ?s) (state ?temp2))

    =>
        (modify ?x (state NO_PLATFORM))
        (modify ?y (state YES_PLATFORM))
        (modify ?z (space ?snew))
)

;-------------------------------------------------------------------------------------
; Moves platform north.
(defrule move_north
    (declare (salience 10))
    ?x<-(space (name ?s) (floor ?temp) (state YES_PLATFORM))
        (north ?s ?snew)
    ?y<-(space (name ?snew) (floor ?temp1) (state NO_PLATFORM))
    ?z<-(platform (name ?pn) (space ?s) (state ?temp2))

    =>
        (modify ?x (state NO_PLATFORM))
        (modify ?y (state YES_PLATFORM))
        (modify ?z (space ?snew))
)

;-------------------------------------------------------------------------------------
; Moves platform south.
(defrule move_south
    (declare (salience 10))
    ?x<-(space (name ?s) (floor ?temp) (state YES_PLATFORM))
        (north ?snew ?s)
    ?y<-(space (name ?snew) (floor ?temp1) (state NO_PLATFORM))
    ?z<-(platform (name ?pn) (space ?s) (state ?temp2))

    =>
        (modify ?x (state NO_PLATFORM))
        (modify ?y (state YES_PLATFORM))
        (modify ?z (space ?snew))
)

;-------------------------------------------------------------------------------------
; Moves platform up.
(defrule change_floor_up
    (declare (salience 10))
    ?x<-(space (name ?s) (floor ?temp) (state YES_PLATFORM))
        (up ?s ?snew)
    ?y<-(space (name ?snew) (floor ?temp1) (state NO_PLATFORM))
    ?z<-(platform (name ?pn) (space ?s) (state ?temp2))

    =>
        (modify ?x (state NO_PLATFORM))
        (modify ?y (state YES_PLATFORM))
        (modify ?z (space ?snew))
)

;-------------------------------------------------------------------------------------
; Moves platform down.
(defrule change_floor_down
    (declare (salience 10))
    ?x<-(space (name ?s) (floor ?temp) (state YES_PLATFORM))
        (up ?snew ?s)
    ?y<-(space (name ?snew) (floor ?temp1) (state NO_PLATFORM))
    ?z<-(platform (name ?pn) (space ?s) (state ?temp2))

    =>
        (modify ?x (state NO_PLATFORM))
        (modify ?y (state YES_PLATFORM))
        (modify ?z (space ?snew))
)

;-------------------------------------------------------------------------------------
; Places a car on a platform.
(defrule enter
    (declare (salience 20))
    ?current_platform <- (platform (name ?temp) (space S2) (state EMPTY))
    ?current_car <- (car (registration_number ?temp1) (state NOT_PARKED))

    =>
        (modify ?current_platform (state NOT_EMPTY))
        (modify ?current_car (state ?temp))
)

;-------------------------------------------------------------------------------------
; Checks if there are no cars waiting.
(defrule goal_found
    (declare (salience 30))
    (not (car (registration_number ?temp) (state NOT_PARKED)))

    =>
        (printout t "GOAL FOUND" crlf)
)

;-------------------------------------------------------------------------------------
; Asks if you want to remove cars.
(defrule mark_for_removal
    (declare (salience 25))
    (not (car (registration_number ?temp) (state NOT_PARKED)))
    =>
        (printout t "Do you want to remove a car? (y/n)" crlf)
        (bind ?option (read))
        (if (eq ?option y)
        then
            (printout t "Give plate to remove" crlf)
            (bind ?plate (read))
            (assert (rmcar (registration_number ?plate) (state FOR_REMOVAL)))
        else
            (printout t "Terminated" crlf)
            (halt)
        )
)

(defrule cars_to_remove
    (declare (salience 20))
    ?c1 <- (rmcar (registration_number ?temp) (state FOR_REMOVAL))
    ?c2 <- (car (registration_number ?temp) (state ?lol))
    ?c3 <- (platform (name ?lol) (space S2) (state ?temp2))

    =>
        (retract ?c1)
        (retract ?c2)
        (modify ?c3 (state EMPTY))
        (printout t "Car Removed" crlf)
        (printout t "Do you want to remove a car? (y/n)" crlf)
        (bind ?option (read))
        (if (eq ?option y)
        then
            (printout t "Give plate to remove" crlf)
            (bind ?plate (read))
            (assert (rmcar (registration_number ?plate) (state FOR_REMOVAL)))
        else
            (printout t "Terminated" crlf)
            (halt)
        )

)

;-------------------------------------------------------------------------------------
; Checks if there are cars waiting and not available platforms.
(defrule goal_failed
    (declare (salience 30))
    (car (registration_number ?temp) (state NOT_PARKED))
    (and (not (platform (name ?temp1) (space ?temp2) (state EMPTY))))

    =>
        (printout t "GOAL FAILED" crlf)
        (halt)
)

;-------------------------------------------------------------------------------------
; Initializing.
; These rules runs first because of salience = 100 is the biggest number.
(defrule initialize
    (declare (salience 100))
    (initial-fact)

    =>
        (set-strategy random)
)

(defrule set_cars
    (declare (salience 100))
    (initial-fact)

    =>
        (printout t "Give number of cars" crlf)
        (bind ?num (read))
        (loop-for-count (?temp 1 ?num) do
            (printout t "Enter car platte" crlf)
            (bind ?car (read))
            (assert (car (registration_number ?car) (state NOT_PARKED)))
        )
)


;;;======================================================
;;;   Automotive Expert System
;;;
;;;     This expert system diagnoses some simple
;;;     problems with a car.
;;;
;;;     CLIPS Version 6.3 Example
;;;
;;;     To execute, merely load, reset and run.
;;;======================================================

;;****************
;;* DEFFUNCTIONS *
;;****************

(deffunction ask-question (?question $?allowed-values)
   (printout t ?question)
   (bind ?answer (read))
   (if (lexemep ?answer) 
       then (bind ?answer (lowcase ?answer)))
   (while (not (member$ ?answer ?allowed-values)) do
      (printout t ?question)
      (bind ?answer (read))
      (if (lexemep ?answer) 
          then (bind ?answer (lowcase ?answer))))
   ?answer)

(deffunction yes-or-no-p (?question)
   (bind ?response (ask-question ?question yes no y n))
   (if (or (eq ?response yes) (eq ?response y))
       then yes 
       else no))

;;;***************
;;;* QUERY RULES *
;;;***************

(defrule determine-cost-is-greater-than-40000-rub ""
   (declare (salience 30))
   (not (cost-is-greater-than-40000-rub ?))
   (not (choose ?))
   =>
   (assert (cost-is-greater-than-40000-rub (yes-or-no-p "Are you ready to spend more than 40 thousand rubles (yes/no)? "))))
   
(defrule determine-whether-a-film-camera ""
	(declare (salience 29))
   (not (is-film-camera ?))
   (not (choose ?))
   =>
   (assert (is-film-camera (yes-or-no-p "Do you need a film camera (yes/no)? "))))

(defrule expensive-and-film-camera ""
   (declare (salience 28))
   (cost-is-greater-than-40000-rub yes)
   (is-film-camera yes)
   (not (choose ?))   
   =>
   (assert (expensive-and-film-camera)))
   
(defrule is-interchangeable-lens
	(declare (salience 27))
	(not (expensive-and-film-camera))
	(not (is-interchangeable-lens ?))
	(not (choose ?))
	=>
	(assert (is-interchangeable-lens (yes-or-no-p "Do you need a camera with interchangeable lens (yes/no)? "))))
	
(defrule cheap-and-not-film-camera
	(declare (salience 26))
	(cost-is-greater-than-40000-rub no)
	(is-film-camera no)
	(not (choose ?))
   =>
   (assert (cheap-and-not-film-camera)))
   
(defrule expensive-and-not-film-camera
	(declare (salience 25))
	(cost-is-greater-than-40000-rub yes)
	(is-film-camera no)
	(not (choose ?))
	=>
	(assert (expensive-and-not-film-camera)))

(defrule is-reflex-camera
	(declare (salience 24))
	(or (expensive-and-not-film-camera)
		(is-interchangeable-lens yes))
	(not (is-reflex-camera ?))
	(not (choose ?))
	=>
	(assert (is-reflex-camera (yes-or-no-p "Do you need a reflex camera (yes/no)? "))))
	
(defrule is-sensor-size
	(declare (salience 23))
	(expensive-and-not-film-camera)
	(not (sensor-size-is ?))
	(not (choose ?))
	=>
	(assert (sensor-size-is (ask-question "What is the size of camera sensor (medium-size/full-frame) ?"
						     medium-size full-frame))))
							 
(defrule cheap-and-film-camera
	(declare (salience 22))
	(cost-is-greater-than-40000-rub no)
	(is-film-camera yes)
	(not (choose ?))
	=>
	(assert (cheap-and-film-camera)))
 
 
(defrule choose-Hasselblad-202FA ""
	(declare (salience 21))
   (expensive-and-film-camera)
   (not (choose ?))
   =>
   (assert (choose Hasselblad-202FA)))
   
 
(defrule cheap-and-not-film-camera-with-interchangeable-lens
    (declare (salience 20))
	(cheap-and-not-film-camera)
	(is-interchangeable-lens yes)
	(not (choose ?))
	=>
	(assert (cheap-and-not-film-camera-with-interchangeable-lens)))

(defrule for-vacation
	(declare (salience 19))
	(is-film-camera no)
	(cost-is-greater-than-40000-rub no)
	(is-interchangeable-lens no)
	(not (is-for-vacation ?))
	(not (choose ?))
	=>
	(assert (is-for-vacation (yes-or-no-p "Do you need a camera for a vacation (yes/no)?"))))
	
(defrule cheap-and-not-film-camera-with-nonchangeable-lens
	(declare (salience 18))
	(cheap-and-not-film-camera)
	(is-interchangeable-lens no)
	(not (choose ?))
	=>
	(assert (cheap-and-not-film-camera-with-nonchangeable-lens)))
	

	
(defrule choose-Pentax-645Z
	(declare (salience 17))
	(expensive-and-not-film-camera)
	(sensor-size-is medium-size)
	(is-reflex-camera yes)
	(not (choose ?))
	=>
	(assert (choose Pentax-645Z)))
	
(defrule choose-Fujifilm-GFX-50S
	(declare (salience 16))
	(expensive-and-not-film-camera)
	(sensor-size-is medium-size)
	(is-reflex-camera no)
	(not (choose ?))
	=>
	(assert (choose Fujifilm-GFX-50S)))	
	
(defrule choose-Canon-EOS-5D-Mark-IV
	(declare (salience 15))
	(expensive-and-not-film-camera)
	(sensor-size-is full-frame)
	(is-reflex-camera yes)
	(not (choose ?))
	=>
	(assert (choose Canon-EOS-5D-Mark-IV)))	
	
	
(defrule choose-Nikon-Z-6
	(declare (salience 14))
	(expensive-and-not-film-camera)
	(sensor-size-is full-frame)
	(is-reflex-camera no)
	(not (choose ?))
	=>
	(assert (choose Nikon-Z-6)))
	

(defrule  choose-Zenit-E
	(declare (salience 13))
	(cheap-and-film-camera)
	(is-interchangeable-lens yes)
	(not (choose ?))
	=>
	(assert (choose Zenit-E)))

(defrule choose-SAMSUNG-fino-800
	(declare (salience 12))
	(cheap-and-film-camera)
	(is-interchangeable-lens no)
	(not (choose ?))
	=>
	(assert (choose SAMSUNG-fino-800)))

	
(defrule choose-Canon-2000D
	(declare (salience 11))
	(cheap-and-not-film-camera-with-interchangeable-lens)
	(is-reflex-camera yes)
	(not (choose ?))
	=>
	(assert (choose Canon-2000D)))	
	
(defrule choose-Fujifilm-X-A20
	(declare (salience 10))
	(cheap-and-not-film-camera-with-interchangeable-lens)
	(is-reflex-camera no)
	(not (choose ?))
	=>
	(assert (choose Fujifilm-X-A20)))

	
(defrule cheap-and-not-film-camera-with-nonchangeable-lens
	(declare (salience 9))
	(cheap-and-not-film-camera)
	(is-interchangeable-lens no)
	(not (choose ?))
	=>
	(assert (cheap-and-not-film-camera-with-nonchangeable-lens)))
	
(defrule for-vacation
	(declare (salience 8))
	(cheap-and-not-film-camera-with-nonchangeable-lens)
	(not (is-for-vacation ?))
	(not (choose ?))
	=>
	(assert (is-for-vacation (yes-or-no-p "Do you need a camera for a vacation (yes/no)?"))))
	
(defrule type-of-vacation-is
	(declare (salience 7))
	(is-for-vacation yes)
	(cheap-and-not-film-camera-with-nonchangeable-lens)
	(not (type-of-vacation ?))
	(not (choose ?))
	=>
	(assert (type-of-vacation (ask-question "What is the type of your vacation (swimming/hiking)? "
							   swimming hiking))))
	
(defrule cheap-and-not-film-camera-with-non-changeable-lens-for-vacation
	(declare (salience 6))
	(cheap-and-not-film-camera-with-nonchangeable-lens)
	(is-for-vacation yes)
	(not (choose ?))
	=>
	(assert (cheap-and-not-film-camera-with-nonchangeable-lens-for-vacation)))
	
(defrule choose-Canon-PowerShot-G9-X-Mark
	(declare (salience 5))
	(cheap-and-not-film-camera-with-nonchangeable-lens)
	(is-for-vacation no)
	(not (choose ?))
	=>
	(assert (choose Canon-PowerShot-G9-X-Mark)))
						
(defrule choose-Nikon-Coolpix-B500
	(declare (salience 4))
	(cheap-and-not-film-camera-with-nonchangeable-lens-for-vacation)
	(type-of-vacation hiking)
	(not (choose ?))
	=>
	(assert (choose Nikon-Coolpix-B500)))
	
(defrule choose-Fujifilm-FinePix-XP130
	(declare (salience 3))
	(cheap-and-not-film-camera-with-nonchangeable-lens-for-vacation)
	(type-of-vacation swimming)
	(not (choose ?))
	=>
	(assert (choose Fujifilm-FinePix-XP130)))



;;;********************************
;;;* STARTUP AND CONCLUSION RULES *
;;;********************************

(defrule system-banner ""
  (declare (salience 35))
  =>
  (printout t crlf crlf)
  (printout t "A camera choice Expert System")
  (printout t crlf crlf))

(defrule print-choose ""
  (declare (salience 35))
  (choose ?item)
  =>
  (printout t crlf crlf)
  (printout t "Suggested choose:")
  (printout t crlf crlf)
  (format t " %s%n%n%n" ?item))


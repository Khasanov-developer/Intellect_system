
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
   (declare (salience 20))
   (not (cost-is-greater-than-40000-rub ?))
   (not (choose ?))
   =>
   (assert (cost-is-greater-than-40000-rub (yes-or-no-p "Are you ready to spend more than 40 thousand rubles (yes/no)? "))))
   
(defrule determine-whether-a-film-camera ""
   (declare (salience 20))
   (not (is-film-camera ?))
   (not (choose ?))
   =>
   (assert (is-film-camera (yes-or-no-p "Do you need a film camera (yes/no)? "))))

(defrule expensive-and-film-camera ""
   (declare (salience 19))
   (cost-is-greater-than-40000-rub yes)
   (is-film-camera yes)
   (not (choose ?))   
   =>
   (assert (expensive-and-film-camera)))
   
(defrule choose-Hasselblad-202FA ""
	(declare (salience 18))
   (expensive-and-film-camera)
   (not (choose ?))
   =>
   (assert (choose Hasselblad-202FA)))
 
(defrule cheap-and-not-film-camera
	(declare (salience 19))
	(cost-is-greater-than-40000-rub no)
	(is-film-camera no)
	(not (choose ?))
   =>
   (assert (cheap-and-not-film-camera)))
   
(defrule is-interchangeable-lens
	(declare (salience 7))
	(not (is-interchangeable-lens ?))
	(not (choose ?))
	=>
	(assert (is-interchangeable-lens (yes-or-no-p "Do you need a camera with interchangeable lens (yes/no)? "))))
	
(defrule cheap-and-not-film-camera-with-interchangeable-lens
	(cheap-and-not-film-camera yes)
	(is-interchangeable-lens yes)
	(not (choose ?))
	=>
	(assert (cheap-and-not-film-camera-with-interchangeable-lens)))

(defrule is-reflex-camera
	(declare (salience 7))
	(not (is-reflex-camera ?))
	(not (choose ?))
	=>
	(assert (is-reflex-camera (yes-or-no-p "Do you need a reflex camera (yes/no)? "))))

(defrule choose-Canon-2000D
	(cheap-and-not-film-camera-with-interchangeable-lens)
	(is-reflex-camera yes)
	(not (choose ?))
	=>
	(assert (choose Canon-2000D)))

(defrule choose-Fujifilm-X-A20
	(cheap-and-not-film-camera-with-interchangeable-lens)
	(is-reflex-camera no)
	(not (choose ?))
	=>
	(assert (choose Fujifilm-X-A20)))
	
(defrule cheap-and-not-film-camera-with-nonchangeable-lens
	(cheap-and-not-film-camera yes)
	(is-interchangeable-lens no)
	(not (choose ?))
	=>
	(assert (cheap-and-not-film-camera-with-nonchangeable-lens)))
	
(defrule for-vacation
	(not (is-for-vacation ?))
	(not (choose ?))
	=>
	(assert (is-for-vacation (yes-or-no-p "Do you need a camera for a vacation (yes/no)?"))))
	
(defrule cheap-and-not-film-camera-with-non-changeable-lens-for-vacation
	(cheap-and-not-film-camera-with-nonchangeable-lens)
	(is-for-vacation yes)
	(not (choose ?))
	=>
	(assert (cheap-and-not-film-camera-with-nonchangeable-lens-for-vacation)))
	
(defrule type-of-vacation-is-swimming
	(not (type-of-vacation ?))
	(not (choose ?))
	=>
	(assert (type-of-vacation (ask-question "What is the type of your vacation (swimming/hiking)? "
							   swimming hiking))))
					
(defrule choose-Nikon-Coolpix-B500
	(cheap-and-not-film-camera-with-nonchangeable-lens-for-vacation)
	(type-of-vacation hiking)
	(not (choose ?))
	=>
	(assert (choose Nikon-Coolpix-B500)))
	
(defrule choose-Fujifilm-FinePix-XP130
	(cheap-and-not-film-camera-with-nonchangeable-lens-for-vacation)
	(type-of-vacation swimming)
	(not (choose ?))
	=>
	(assert (choose Fujifilm-FinePix-XP130)))
	
(defrule choose-Canon-PowerShot-G9-X-Mark
	(cheap-and-not-film-camera-with-nonchangeable-lens)
	(is-for-vacation no)
	(not (choose ?))
	=>
	(assert (choose Canon-PowerShot-G9-X-Mark)))
	
(defrule expensive-and-not-film-camera
	(declare (salience 19))
	(cost-is-greater-than-40000-rub yes)
	(is-film-camera no)
	(not (choose ?))
	=>
	(assert (expensive-and-not-film-camera)))
	
(defrule is-sensor-size
	(not (sensor-size-is ?))
	(not (choose ?))
	=>
	(assert (sensor-size-is (ask-question "What is the size of camera sensor (medium-size/full-frame) ?"
						     medium-size full-frame))))

(defrule choose-Pentax-645Z
	(expensive-and-not-film-camera)
	(sensor-size-is medium-size)
	(is-reflex-camera yes)
	(not (choose ?))
	=>
	(assert (choose Pentax-645Z)))
	
(defrule choose-Fujifilm-GFX-50S
	(expensive-and-not-film-camera)
	(sensor-size-is medium-size)
	(is-reflex-camera no)
	(not (choose ?))
	=>
	(assert (choose Fujifilm-GFX-50S)))
	
(defrule choose-Canon-EOS-5D-Mark-IV
	(expensive-and-not-film-camera)
	(sensor-size-is full-frame)
	(is-reflex-camera yes)
	(not (choose ?))
	=>
	(assert (choose Canon-EOS-5D-Mark-IV)))
	
(defrule choose-Nikon-Z-6
	(expensive-and-not-film-camera)
	(sensor-size-is full-frame)
	(is-reflex-camera no)
	(not (choose ?))
	=>
	(assert (choose Nikon-Z-6)))
	
(defrule cheap-and-film-camera
	(declare (salience 19))
	(cost-is-greater-than-40000-rub no)
	(is-film-camera yes)
	(not (choose ?))
	=>
	(assert (cheap-and-film-camera)))
	
(defrule  choose-Zenit-E
	(cheap-and-film-camera)
	(is-interchangeable-lens yes)
	(not (choose ?))
	=>
	(assert (choose Zenit-E)))
	
(defrule choose-SAMSUNG-fino-800
	(cheap-and-film-camera)
	(is-interchangeable-lens no)
	(not (choose ?))
	=>
	(assert (choose SAMSUNG-fino-800)))

;;;********************************
;;;* STARTUP AND CONCLUSION RULES *
;;;********************************

(defrule system-banner ""
  (declare (salience 25))
  =>
  (printout t crlf crlf)
  (printout t "A camera choice Expert System")
  (printout t crlf crlf))

(defrule print-choose ""
  (declare (salience 25))
  (choose ?item)
  =>
  (printout t crlf crlf)
  (printout t "Suggested choose:")
  (printout t crlf crlf)
  (format t " %s%n%n%n" ?item))


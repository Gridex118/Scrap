(println "Guess the Number!")

(defn input []
  (print "Enter any number: ")
  (flush)
  (Integer/parseInt (read-line)))

(let [number (rand-int 100)]
  (defn check [guess]
    (cond
      (> guess number)
      (do
        (println "Too High...")
        false)
      (< guess number)
      (do
        (println "...Too Low")
        false)
      :else true))
  (while (not (check (input))))
  (println "You Got It!"))

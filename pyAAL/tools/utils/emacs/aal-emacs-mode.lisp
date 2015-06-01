
;; define several class of keywords
(setq aal-keywords '("AGENT" "apply" "auditing" "behavior" "call" "check" "clause" "data" "exec" "if_violated_then" "load" "macro" "of" "service" "type" "types") )
(setq aal-types '("float" "integer" "key" "list" "rotation" "string" "vector"))
(setq aal-constants '("always" "must" "mustnot" "never" "sometime" "until"))
(setq aal-events '("after" "and" "before" "exists" "forall" "if" "not" "onlywhen" "or" "then" "where"))
(setq aal-functions '("ae" "actions" "attributes" "deny" "extends" "get_audit" "get_rectification" "get_usage" "permit" "provided" "ps" "purpose" "re" "required" "rs" "subject" "ue"))

;; create the regex string for each class of keywords
(setq aal-keywords-regexp (regexp-opt aal-keywords 'words))
(setq aal-type-regexp (regexp-opt aal-types 'words))
(setq aal-constant-regexp (regexp-opt aal-constants 'words))
(setq aal-event-regexp (regexp-opt aal-events 'words))
(setq aal-functions-regexp (regexp-opt aal-functions 'words))

;; clear memory
(setq aal-keywords nil)
(setq aal-types nil)
(setq aal-constants nil)
(setq aal-events nil)
(setq aal-functions nil)

;; create the list for font-lock.
;; each class of keyword is given a particular face
(setq aal-font-lock-keywords
  `(
    (,aal-type-regexp . font-lock-type-face)
    (,aal-constant-regexp . font-lock-constant-face)
    (,aal-event-regexp . font-lock-builtin-face)
    (,aal-functions-regexp . font-lock-function-name-face)
    (,aal-keywords-regexp . font-lock-keyword-face)
    ;; note: order above matters. “aal-keywords-regexp” goes last because
    ;; otherwise the keyword “state” in the function “state_entry”
    ;; would be highlighted.
))

;; define the mode
(define-derived-mode aal-mode fundamental-mode
  "aal mode"
  "Major mode for editing AAL (Abstract Accountability Language)…"

  ;; code for syntax highlighting
  (setq font-lock-defaults '((aal-font-lock-keywords)))

  ;; clear memory
  (setq aal-keywords-regexp nil)
  (setq aal-types-regexp nil)
  (setq aal-constants-regexp nil)
  (setq aal-events-regexp nil)
  (setq aal-functions-regexp nil)
)

(provide 'aal-mode)

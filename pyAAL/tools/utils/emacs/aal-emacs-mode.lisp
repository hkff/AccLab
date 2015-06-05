;; define several class of keywords
(setq aal-keywords '("AGENT" "APPLY" "AUDITING" "BEHAVIOR" "CALL" "CHECK" "CLAUSE" "DATA" "EXEC" "IF_VIOLATED_THEN" "LOAD" "MACRO" "OF" "SERVICE" "TYPE" "TYPES" "," "AFTER" "AND" "BEFORE" "EXISTS" "FORALL" "IF" "NOT" "ONLYWHEN" "OR" "THEN" "WHERE" "PROVIDED" "PS" "PURPOSE" "REQUIRED" "RS") )
(setq aal-types '("Actor" "DataSubject" "DataController" "DataProcessor" "DwDataController" "Auditor" "CloudProvider" "CloudCustomer" "EndUser"))
(setq aal-constants '("ALWAYS" "MUST" "MUSTNOT" "NEVER" "SOMETIME" "UNTIL" "UNLESS" "NEXT"))
(setq aal-events '())
(setq aal-functions '("ae" "actions" "attributes" "DENY" "EXTENDS" "get_audit" "get_rectification" "get_usage" "PERMIT"
 "re" "subject" "ue"))

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

;; command to comment/uncomment text
(defun aal-comment-dwim (arg)
  "Comment or uncomment current line or region in a smart way.
For detail, see `comment-dwim'."
  (interactive "*P")
  (require 'newcomment)
  (let (
        (comment-start "//") (comment-end " ")
        )
    (comment-dwim arg)))

;; syntax table
(defvar aal-syntax-table nil "Syntax table for `aal-mode'.")
(setq aal-syntax-table
      (let ((synTable (make-syntax-table)))
	(modify-syntax-entry ?\n "> b" synTable)
	(modify-syntax-entry ?\/ ". 12b" synTable)
	(modify-syntax-entry ?\/ ". 14" synTable)
	(modify-syntax-entry ?* ". 23" synTable)
        synTable))

;; define the mode
(define-derived-mode aal-mode prog-mode
  "aal mode"
  "Major mode for editing AAL (Abstract Accountability Language)…"
  :syntax-table aal-syntax-table

  ;; code for syntax highlighting
  (setq font-lock-defaults '((aal-font-lock-keywords)))
  (define-key aal-mode-map [remap comment-dwim] 'aal-comment-dwim)

  ;; clear memory
  (setq aal-keywords-regexp nil)
  (setq aal-types-regexp nil)
  (setq aal-constants-regexp nil)
  (setq aal-events-regexp nil)
  (setq aal-functions-regexp nil)
)

(provide 'aal-mode)

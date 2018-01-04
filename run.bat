@echo OFF
chcp 65001 > nul
title Utilitário

set /p month="Mês do checklist: "
set /p year="Ano do checklist: "
python -m crawler %year% %month%
from pst import PstDB


year = '2025'
issue = 30


pst_db = PstDB(data_pth='data', issue=issue, year=year)

## добавление статьи
# pst_db.add_article(art_fn='art_89.yaml')

## проставляем edn
# pst_db.add_edn2art(issue=issue)

## проставляем даты
# pst_db.add_date2art(issue=issue, date_field='accepted', date4insert='31.10.2025')

## проверка пропусков в метаданных
# pst_db.empty_spaces(issue=issue)

## печать списка авторов
# pst_db.print_author()

## статистика по выпуску
# pst_db.get_statistics(issue)

## статьи в выпуске
# pst_db.get_art_in_iss(issue)

## формирование метаданных для выпуска
pst_db.make_docx(issue=issue)


#
# curr_art = get_articles('articles')

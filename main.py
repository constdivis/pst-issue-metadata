from pst import PstDB

year = '2025'
issue = 30

pst_db = PstDB(data_pth='data', issue=issue, year=year)




# pst_db.add_article(art_fn='a75.yaml')
# pst_db.add_article(art_fn='art_74.yaml')
# pst_db.add_article(art_fn='art_76.yaml')
# pst_db.add_article(art_fn='art_77.yaml')
# pst_db.add_article(art_fn='art_80.yaml')
# pst_db.add_article(art_fn='art_81.yaml')
# pst_db.add_article(art_fn='art_82.yaml')
# pst_db.add_article(art_fn='art_89.yaml')
#
#
# pst_db.add_edn2art(issue=issue)
# pst_db.add_date2art(issue=issue, date_field='accepted', date4insert='31.10.2025')
# pst_db.empty_spaces(issue=issue)
# # #
# pst_db.print_author()
# pst_db.get_statistics(issue)
pst_db.get_art_in_iss(issue)
pst_db.make_docx(issue=issue)
# # #
#
# curr_art = get_articles('articles')




















# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

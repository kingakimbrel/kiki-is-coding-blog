from django.db import connection
import calendar

from blog_app.models import Post, ArchiveMonthNode, ArchiveYearNode

def get_archive():
    """Builds the year/month based archive tree."""
    archive = []

    with connection.cursor() as cursor:
        # postgres
        cursor.execute('SELECT extract(year from date_added) AS YEAR, '
                       'extract(month from date_added) AS MONTH, '
                       'COUNT(*) AS TOTAL '
                       'FROM blog_app_post '
                       'GROUP BY YEAR, MONTH '
                       'Order by YEAR DESC, MONTH')

        # sql lite
        # cursor.execute('SELECT strftime(\'%Y\', date_added) AS YEAR, '
        #                'strftime(\'%m\', date_added) AS MONTH, '
        #                'COUNT(*) AS TOTAL '
        #                'FROM blog_app_post '
        #                'GROUP BY YEAR, MONTH '
        #                'Order by YEAR DESC, MONTH')

        years = set()
        year_node = ArchiveYearNode()

        for row in cursor.fetchall():

            if not int(row[0]) in years:
                year_node = ArchiveYearNode()
                year_node.year = int(row[0])
                years.add(year_node.year)
                archive.append(year_node)

            print(row)
            month_node = ArchiveMonthNode()
            month_node.month_num = int(row[1])
            month_node.month = calendar.month_name[month_node.month_num]
            month_node.count = int(row[2])

            year_node.months.append(month_node)

    return archive


def get_latest_post():
    """Gets few latest posts."""
    last5posts = Post.objects.defer("text").order_by('-date_added')[:5]
    return last5posts

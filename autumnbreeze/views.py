import csv
import collections
import itertools

from django.shortcuts import render, render_to_response
from django.template import RequestContext

from autumnbreeze.forms import AnomalyForm
from autumnbreeze.models import ComparingOption


def main(request):
    if request.method == "POST":
        form = AnomalyForm(request.POST, request.FILES)
        if form.is_valid():
            # all of the csv file parsing logic is present here:
            comparing_option = ComparingOption.objects.get(
                id=request.POST['comparing_option']
            )

            baseline_file = csv.reader(request.FILES['baseline_file'])
            file_to_compare = csv.reader(request.FILES['file_to_compare'])

            # skip the headers
            next(baseline_file)
            next(file_to_compare)

            # create two iterators for each file using tee(),
            # because iterators expire after they're used:
            baselinefile_it1, baselinefile_it2 = itertools.tee(
                baseline_file, 2
            )
            comparedfile_it1, comparedfile_it2 = itertools.tee(
                file_to_compare, 2
            )

            # find out different days in files:
            different_baseline_days = []
            different_comparedfile_days = []

            for row in baselinefile_it1:
                if row[2] not in different_baseline_days:
                    different_baseline_days.append(row[2])
            for row in comparedfile_it1:
                if row[2] not in different_comparedfile_days:
                    different_comparedfile_days.append(row[2])

            # main datasets that will hold the refferences to location_ids and
            # actual rows:
            baseline_file_data = collections.OrderedDict()
            compared_file_data = collections.OrderedDict()

            # 1st file:
            for i, row in enumerate(baselinefile_it2):
                # make sure we're using correct number of days from the first
                # file:
                if row[2] in different_baseline_days[
                    :comparing_option.baseline_days
                ]:
                    if row[0] not in baseline_file_data:
                        baseline_file_data[row[0]] = []
                    baseline_file_data[row[0]].append(row)

            # 2nd file:
            for i, row in enumerate(comparedfile_it2):
                # make sure we're using correct number of days from the second
                # file:
                if row[2] in different_comparedfile_days[
                    :comparing_option.days_to_compare
                ]:
                    if row[0] not in compared_file_data:
                        compared_file_data[row[0]] = []
                    compared_file_data[row[0]].append(row)

            # find new location_ids:
            new_location_ids = []
            for location_id, actual_row in compared_file_data.iteritems():
                if location_id not in baseline_file_data:
                    new_location_ids.append(location_id)

            # compare two dictonaries and find new location_ids and data
            # fluctuations:

            # final datasets that will store percentage increase and actual
            # rows:
            data_fluctuations = collections.OrderedDict()

            for location_id, row in compared_file_data.iteritems():
                # make sure we're only dealing with location ids that exist
                # in both files:
                if location_id in baseline_file_data:
                    percentage_increase = 100 * (
                        len(row) - len(baseline_file_data[location_id])
                    ) / len(baseline_file_data[location_id])
                    # only count *increased* fluctuation (because this is a
                    # test task):
                    if percentage_increase <= comparing_option.fluctuation:
                        data_fluctuations[location_id] = ''.join(
                            [str(percentage_increase), '%']
                        )

            print(data_fluctuations)
            print(baseline_file_data['3'])

            # raise Exception('on purpose')

            context = {
                'baseline_file_data': baseline_file_data,
                'compared_file_data': compared_file_data,
                'data_fluctuations': data_fluctuations,
                'new_location_ids': new_location_ids,
            }

            return render_to_response(
                "results.html",
                context,
                context_instance=RequestContext(request)
            )
        else:
            context = {"form": form}
            return render_to_response(
                "main.html",
                context,
                context_instance=RequestContext(request)
            )
    else:
        form = AnomalyForm()
        context = {"form": form}
        return render_to_response(
            "main.html",
            context,
            context_instance=RequestContext(request)
        )
    return render(request, 'main.html', {})


def results(request):
    return render(request, 'results.html', {})

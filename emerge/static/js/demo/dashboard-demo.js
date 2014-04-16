$(function() {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            period: '2010 Q1',
            total: 2666,
            reading: null,
            numeracy: 2647
        }, {
            period: '2010 Q2',
            total: 2778,
            reading: 2294,
            numeracy: 2441
        }, {
            period: '2010 Q3',
            total: 4912,
            reading: 1969,
            numeracy: 2501
        }, {
            period: '2010 Q4',
            total: 3767,
            reading: 3597,
            numeracy: 5689
        }, {
            period: '2011 Q1',
            total: 6810,
            reading: 1914,
            numeracy: 2293
        }, {
            period: '2011 Q2',
            total: 5670,
            reading: 4293,
            numeracy: 1881
        }, {
            period: '2011 Q3',
            total: 4820,
            reading: 3795,
            numeracy: 1588
        }, {
            period: '2011 Q4',
            total: 15073,
            reading: 5967,
            numeracy: 5175
        }, {
            period: '2012 Q1',
            total: 10687,
            reading: 4460,
            numeracy: 2028
        }, {
            period: '2012 Q2',
            total: 8432,
            reading: 5713,
            numeracy: 1791
        }],
        xkey: 'period',
        ykeys: ['total', 'reading', 'numeracy'],
        labels: ['total', 'reading', 'numeracy'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });

    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "Download Sales",
            value: 12
        }, {
            label: "In-Store Sales",
            value: 30
        }, {
            label: "Mail-Order Sales",
            value: 20
        }],
        resize: true
    });

    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            y: '2006',
            a: 100,
            b: 90
        }, {
            y: '2007',
            a: 75,
            b: 65
        }, {
            y: '2008',
            a: 50,
            b: 40
        }, {
            y: '2009',
            a: 75,
            b: 65
        }, {
            y: '2010',
            a: 50,
            b: 40
        }, {
            y: '2011',
            a: 75,
            b: 65
        }, {
            y: '2012',
            a: 100,
            b: 90
        }],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Series A', 'Series B'],
        hideHover: 'auto',
        resize: true
    });

});

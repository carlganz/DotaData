$('#example2').cascadingDropdown({
    selectBoxes: [
        {
            selector: '.step1',
            source: [
                { label: 'Account ID', 'value: account_id' },
                { label: 'Hero', value: 'hero' },
                { label: 'Game Type', value: 'game_type' },
                { label: 'Lobby Type', value: 'lobby_type' }
            ]
        },
        {
            selector: '.step2',
            requires: ['.step1'],
            source: function(request, response) {
                $.getJSON('/api/resolutions', request, function(data) {
                    var selectOnlyOption = data.length <= 1;
                    response($.map(data, function(item, index) {
                        return {
                            label: item,
                            value: item,
                            selected: selectOnlyOption // Select if only option
                        };
                    }));
                });
            }
        },
        {
            selector: '.step3',
            requires: ['.step1', '.step2'],
            requireAll: true,
            source: function(request, response) {
                $.getJSON('/api/storages', request, function(data) {
                    response($.map(data, function(item, index) {
                        return {
                            label: item + ' GB',
                            value: item,
                            selected: index == 0 // Select first available option
                        };
                    }));
                });
            },
            onChange: function(event, value, requiredValues){
                // do stuff
            }
        }
    ]
});

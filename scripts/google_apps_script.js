/**
 * HIYU ABYSS — GOOGLE APPS SCRIPT CHO EDITORIAL DASHBOARD
 * 
 * Hướng dẫn cài đặt:
 * 1. Mở Google Sheet "Hiyu Abyss — Editorial Dashboard"
 * 2. Trên thanh menu, chọn: Tiện ích mở rộng (Extensions) -> Apps Script
 * 3. Xóa code mặc định và dán toàn bộ nội dung file này vào.
 * 4. Bấm Lưu (Ctrl + S) và đóng tab.
 */

function onEdit(e) {
  var sheet = e.source.getActiveSheet();
  if (sheet.getName() !== "TikTok Pipeline") return;
  
  var range = e.range;
  var col = range.getColumn(); // Cột I là cột số 9 (Trạng thái)
  var row = range.getRow();
  
  if (row <= 1) return; // Bỏ qua dòng tiêu đề
  
  // 1. Tự động đổi màu ô Trạng thái (Cột I)
  if (col === 9) {
    var status = range.getValue();
    if (status === "APPROVED") {
      range.setBackground("#D1FAE5"); // Xanh lá pastel
      range.setFontColor("#065F46");
      range.setFontWeight("bold");
    } else if (status === "IN_REVIEW") {
      range.setBackground("#FEF3C7"); // Vàng cam pastel
      range.setFontColor("#92400E");
      range.setFontWeight("bold");
    } else if (status === "REVISE") {
      range.setBackground("#FEE2E2"); // Đỏ nhạt
      range.setFontColor("#991B1B");
      range.setFontWeight("bold");
    } else if (status === "PUBLISHED") {
      range.setBackground("#E0E7FF"); // Tím xanh nhạt
      range.setFontColor("#3730A3");
      range.setFontWeight("bold");
    } else if (status === "REJECTED") {
      range.setBackground("#F3F4F6"); // Xám nhạt
      range.setFontColor("#4B5563");
      range.setFontWeight("normal");
    }
  }
}

/**
 * Menu tùy chỉnh trên Google Sheets
 */
function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('⚡ Hiyu Abyss')
    .addItem('Cập nhật màu sắc trạng thái', 'formatAllStatuses')
    .addItem('Tự động căn chỉnh độ rộng cột', 'autoResizeAllColumns')
    .addToUi();
}

/**
 * Quét toàn bộ cột Trạng thái và định dạng màu
 */
function formatAllStatuses() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("TikTok Pipeline");
  if (!sheet) return;
  
  var lastRow = sheet.getLastRow();
  if (lastRow <= 1) return;
  
  var range = sheet.getRange(2, 9, lastRow - 1, 1);
  var values = range.getValues();
  
  for (var i = 0; i < values.length; i++) {
    var cell = sheet.getRange(i + 2, 9);
    var status = values[i][0];
    if (status === "APPROVED") {
      cell.setBackground("#D1FAE5").setFontColor("#065F46").setFontWeight("bold");
    } else if (status === "IN_REVIEW") {
      cell.setBackground("#FEF3C7").setFontColor("#92400E").setFontWeight("bold");
    } else if (status === "REVISE") {
      cell.setBackground("#FEE2E2").setFontColor("#991B1B").setFontWeight("bold");
    } else if (status === "PUBLISHED") {
      cell.setBackground("#E0E7FF").setFontColor("#3730A3").setFontWeight("bold");
    }
  }
}

/**
 * Tự động căn chỉnh độ rộng toàn bộ các cột
 */
function autoResizeAllColumns() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("TikTok Pipeline");
  if (!sheet) return;
  for (var i = 1; i <= 12; i++) {
    sheet.autoResizeColumn(i);
  }
}
